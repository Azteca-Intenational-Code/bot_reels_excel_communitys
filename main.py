import subprocess
from config import SessionLocal
from sqlalchemy import text as sql_text
from GptAPi import GPT
from openpyxl import load_workbook
from calendar import month_name
from datetime import datetime, timedelta
import shutil
import random
import os

# Configuración
plantilla_path = "Archivo de prueba reels para Niyi.xlsx"
fecha_actual = datetime.today()
reels_por_campaña = 30
carpeta_destino = "excel_campañas"
mes_actual = datetime.today().month
nombre_mes_actual = month_name[mes_actual]

if not os.path.exists(carpeta_destino):
    os.makedirs(carpeta_destino)

with SessionLocal() as session:
    result = session.execute(sql_text("SELECT campaign, commercial_services, residential_services, language FROM campaign"))
    rows = result.fetchall()

# rows = [row for row in rows if row[0].strip().lower() == "elite chicago spa"]

# if not rows:
#     print("⚠️ La campaña 'Elite Chicago Spa' no fue encontrada en la base de datos.")
#     exit()


dias_semana = {
    0: "lunes", 1: "martes", 2: "miércoles", 3: "jueves",
    4: "viernes", 5: "sábado", 6: "domingo"
}

for row in rows:
    campaign_name, commercial_services, residential_services, lang = row
    campaign_key = campaign_name.lower().replace(" ", "_")
    print(f"\n📢 Procesando campaña: {campaign_name} [{campaign_key}]")

    excel_path = os.path.join(carpeta_destino, f"Reels_{campaign_key}.xlsx")
    if os.path.exists(excel_path):
        wb = load_workbook(excel_path)
        ws = wb.active
    else:
        shutil.copy(plantilla_path, excel_path)
        wb = load_workbook(excel_path)
        ws = wb.active

    headers = [cell.value for cell in ws[1]]
    for col in ["Picture Url 1", "Time", "Facebook Title"]:
        if col not in headers:
            headers.append(col)
            ws.cell(row=1, column=len(headers)).value = col
    
    post_generados = 0
    idx_text = headers.index("Text") + 1
    idx_date = headers.index("Date") + 1
    idx_title = headers.index("Document title") + 1
    idx_yt_title = headers.index("Youtube Video Title") + 1
    idx_yt_tags = headers.index("Youtube Video Tags") + 1
    idx_fb_title = headers.index("Facebook Title") + 1
    idx_comment = headers.index("First Comment Text") + 1
    idx_tiktok = headers.index("TikTok Title") + 1
    idx_picture = headers.index("Picture Url 1") + 1
    idx_time = headers.index("Time") + 1
    idx_brand = headers.index("Brand name") + 1 if "Brand name" in headers else None

    cols_autoincrement = [
        "Document title", "Youtube Video Title", "Youtube Video Tags",
        "Facebook Title", "TikTok Title"
    ]

    idx_autoincrement = {
        col: headers.index(col) + 1 for col in cols_autoincrement if col in headers
    }

    with SessionLocal() as session:
        result = session.execute(sql_text("""
            SELECT id FROM campaign WHERE LOWER(TRIM(campaign)) = :nombre
        """), {"nombre": campaign_name.lower().strip()})
        row = result.fetchone()
        if row:
            id_campania = row[0]
        else:
            print(f"❌ No se encontró el ID para la campaña '{campaign_name}'")
            exit()

        result = session.execute(sql_text("""
            SELECT theme, event, focus, suggestions, date
            FROM annual_schedule
            WHERE id_campaign = :id AND LOWER(TRIM(month)) = :mes
        """), {"id": id_campania, "mes": nombre_mes_actual.lower().strip()})

        evento_db = result.fetchone()
        if not evento_db:
            print(f"⚠️ No hay información en annual_schedule para el mes {mes_actual} y campaña ID {id_campania}")
            theme_event = evento_principal = focus = suggestions = "No aplica"
        else:
            theme_event, event, focus, suggestions, fecha_evento = evento_db
            eventos = event.split(", ") if event else []

            # Validar si la fecha ya pasó
            if fecha_evento and fecha_evento < datetime.today().date():
                print(f"📆 La fecha del evento {fecha_evento} ya pasó. No se promocionará.")
                evento_principal = "No aplica"
            else:
                evento_principal = eventos[0].strip() if eventos else "No aplica"

    print(f"\n📢 Tema campaña: {theme_event}")
    print(f"\n📢 Evento campaña: {event}]")
    print(f"\n📢 focus campaña: {focus}]")
    print(f"\n📢 suggestions campaña: {suggestions}]")

    reels_generados = 0
    while reels_generados < reels_por_campaña:
        opciones_servicios = []
        if commercial_services:
            opciones_servicios.append(commercial_services)
        if residential_services:
            opciones_servicios.append(residential_services)
        if not opciones_servicios:
            print(f"⚠️ No hay servicios en {campaign_name}")
            break

        servicio = random.choice(random.choice(opciones_servicios).split(", "))
        print(f"📌 Servicio elegido: {servicio}")
        gpt = GPT({"service": servicio, "campaign": campaign_key, "lang": lang.lower()})

        if campaign_key == "osceola_fence_company":
            theme = gpt.theme_osceola()
            data = {
                "Text": gpt.copy_osceola(theme, 100),
                "Document title": gpt.document_title_osceola(theme),
                "Youtube Video Title": gpt.youtube_video_title_osceola(theme, 40),
                "Youtube Video Tags": gpt.youtube_video_tags_osceola(theme),
                "First Comment Text": gpt.firts_comment_osceola(theme, 50),
                "TikTok Title": gpt.tikTok_title_osceola(theme, 50),
            }

        elif campaign_key == "quick_cleaning":
            theme = gpt.theme_quick_cleaning()
            data = {
                "Text": gpt.copy_quick_cleaning(theme, 100),
                "Document title": gpt.document_title_quick_cleaning(theme),
                "Youtube Video Title": gpt.youtube_video_title_quick_cleaning(theme),
                "Youtube Video Tags": gpt.youtube_video_tags_quick_cleaning(theme),
                "First Comment Text": gpt.firts_comment_quick_cleaning(theme, 50),
                "TikTok Title": gpt.tikTok_title_quick_cleaning(theme, 50),
            }

        elif campaign_key == "elite_chicago_spa":
            theme = gpt.theme_elite_spa()
            data = {
                "Text": gpt.copy_elite_spa(theme, 100),
                "Document title": gpt.document_title_elite_spa(theme),
                "Youtube Video Title": gpt.youtube_video_title_elite_spa(theme),
                "Youtube Video Tags": gpt.youtube_video_tags_elite_spa(theme),
                "First Comment Text": gpt.firts_comment_elite_spa(theme, 50),
                "TikTok Title": gpt.tikTok_title_elite_spa(theme, 50),
            }

        elif campaign_key == "lopez_y_lopez_abogados":
            theme = gpt.theme_lopez_abogados()
            data = {
                "Text": gpt.copy_lopez_abogados(theme, 100),
                "Document title": gpt.document_title_lopez_abogados(theme),
                "Youtube Video Title": gpt.youtube_video_title_lopez_abogados(theme),
                "Youtube Video Tags": gpt.youtube_video_tags_lopez_abogados(theme),
                "First Comment Text": gpt.firts_comment_lopez_abogados(theme, 50),
                "TikTok Title": gpt.tikTok_title_lopez_abogados(theme, 50),
            }

        elif campaign_key.startswith("botánica"):
            theme = gpt.theme_botanica()
            data = {
                "Text": gpt.copy_botanica(theme, 100),
                "Document title": gpt.document_title_botanica(theme),
                "Youtube Video Title": gpt.youtube_video_title_botanica(theme, 50),
                "Youtube Video Tags": gpt.youtube_video_tags_botanica(theme),
                "First Comment Text": gpt.firts_comment_botanica(theme, 50),
                "TikTok Title": gpt.tikTok_title_botanica(theme, 50),
            }

        elif campaign_key.startswith("botanica"):
            theme = gpt.theme_botanica()
            data = {
                "Text": gpt.copy_botanica(theme, 100),
                "Document title": gpt.document_title_botanica(theme),
                "Youtube Video Title": gpt.youtube_video_title_botanica(theme, 50),
                "Youtube Video Tags": gpt.youtube_video_tags_botanica(theme),
                "First Comment Text": gpt.firts_comment_botanica(theme, 50),
                "TikTok Title": gpt.tikTok_title_botanica(theme, 50),
            }

        elif campaign_key.startswith("amarres_chicago"):
            theme = gpt.theme_botanica()
            data = {
                "Text": gpt.copy_botanica(theme, 100),
                "Document title": gpt.document_title_botanica(theme),
                "Youtube Video Title": gpt.youtube_video_title_botanica(theme, 50),
                "Youtube Video Tags": gpt.youtube_video_tags_botanica(theme),
                "First Comment Text": gpt.firts_comment_botanica(theme, 50),
                "TikTok Title": gpt.tikTok_title_botanica(theme, 50),
            }

        else:
            print(f"⚠️ Campaña '{campaign_key}' no tiene métodos aún.")
            continue

        print("📥 Texto (Text):", data["Text"])
        print("📄 Título:", data["Document title"])
        plataforma = random.choice(["youtube shorts", "instagram reels"])

        try:
            print("🚀 Ejecutando bot 2...")
            subprocess.run(
                [
                    "python", "main.py",
                    data["Text"],
                    plataforma,
                    data["Document title"],
                    campaign_key,
                    lang,
                    theme_event,
                    evento_principal,
                    focus,
                    suggestions,
                    servicio
                ],
                cwd=r"C:\\Users\\DESARROLLADOR\\Documents\\Manuel Cardona\\bot_creacion_reels",
                check=True,
                timeout=900
            )
        except subprocess.CalledProcessError as e:
            print(f"❌ Error al ejecutar bot 2: {e}")
            break

        reels_generados += 1

    print("📂 Generando Excel desde base de datos...")
    with SessionLocal() as session:
        query = sql_text("""
            SELECT description, platform_video, url_drive 
            FROM videos 
            WHERE campaign = :camp AND upload_drive = true 
            ORDER BY id
        """)
        resultados = session.execute(query, {"camp": campaign_key}).fetchall()

        for i, fila_db in enumerate(resultados):
            descripcion, plataforma, url = fila_db
            fecha_reel = fecha_actual + timedelta(days=i)
            dia_nombre = dias_semana[fecha_reel.weekday()]

            horario_query = sql_text("""
                SELECT hour FROM schedules 
                WHERE platform_video = :plat AND day = :dia
            """)
            schedules = session.execute(horario_query, {"plat": plataforma, "dia": dia_nombre}).fetchall()
            hora_final = "00:00:00"
            if schedules:
                horarios_validos = [h[0] for h in schedules]

                # Si el reel es para hoy, filtra horarios mayores o iguales a la hora actual
                if fecha_reel.date() == datetime.today().date():
                    ahora = datetime.now().time()
                    horarios_validos = [h for h in horarios_validos if h >= ahora]
                    if not horarios_validos:
                        print("⚠️ No hay horarios disponibles posteriores a la hora actual. Usando el primero disponible.")
                        horarios_validos = [h[0] for h in schedules]

                horario_elegido = random.choice(horarios_validos)
                hora_final = horario_elegido.strftime("%H:%M:%S")

            gpt = GPT({"service": "comentario", "campaign": campaign_key, "lang": lang.lower()})
            comentario = gpt.comment_from_title(f"{campaign_key.title()} Video")  # Genera primer comentario

            for row in range(2, ws.max_row + 1):
                if not ws.cell(row=row, column=idx_text).value:
                    ws.cell(row=row, column=idx_text).value = descripcion
                    ws.cell(row=row, column=idx_date).value = fecha_reel.strftime("%Y-%m-%d")
                    ws.cell(row=row, column=idx_title).value = str(post_generados + 1)
                    ws.cell(row=row, column=idx_yt_title).value = str(post_generados + 1)
                    ws.cell(row=row, column=idx_yt_tags).value = str(post_generados + 1)
                    ws.cell(row=row, column=idx_fb_title).value = str(post_generados + 1)
                    ws.cell(row=row, column=idx_tiktok).value = str(post_generados + 1)
                    ws.cell(row=row, column=idx_comment).value = comentario
                    ws.cell(row=row, column=idx_picture).value = url
                    ws.cell(row=row, column=idx_time).value = hora_final
                    if idx_brand:
                        ws.cell(row=row, column=idx_brand).value = campaign_name
                    for idx_col in idx_autoincrement.values():
                        ws.cell(row=row, column=idx_col).value = str(post_generados + 1)
                    print(f"✅ Fila {row} completada.")
                    post_generados += 1
                    break

        # ✅ Elimina filas vacías (donde la celda 'Text' está vacía)
        max_row = ws.max_row
        for row in range(max_row, 1, -1):
            if not ws.cell(row=row, column=idx_text).value:
                ws.delete_rows(row)
        # Guarda Excel normal
        wb.save(excel_path)
        print(f"📊 Excel guardado: {excel_path}")

        # Convierte como CSV duplicando los datos del Excel
        csv_path = excel_path.replace(".xlsx", ".csv")
        with open(csv_path, "w", encoding="utf-8", newline="") as f:
            from csv import writer
            csv_writer = writer(f)

            # Escribir encabezados
            csv_writer.writerow([cell.value for cell in ws[1]])

            # Escribir filas
            for row in ws.iter_rows(min_row=2, values_only=True):
                csv_writer.writerow(row)

        print(f"📄 También guardado como CSV: {csv_path}")

print("\n✅ Todas las campañas han sido procesadas.")

try:
    print("🚀 Ejecutando bot 3 para subir excels a Metricool...")
    subprocess.run(
        ["python", "main.py"],
        cwd=r"C:\\Users\\DESARROLLADOR\\Documents\\Manuel Cardona\\bot_metricool",
        check=True
    )
except subprocess.CalledProcessError as e:
    print(f"❌ Error al ejecutar bot 3: {e}")