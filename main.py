import subprocess
from config import SessionLocal
from sqlalchemy import text as sql_text
from GptAPi import GPT
from openpyxl import load_workbook
from datetime import datetime, timedelta
import shutil
import random
import os

# Configuración
plantilla_path = "Archivo de prueba reels para Niyi.xlsx"
fecha_actual = datetime.today()
reels_por_campaña = 2
carpeta_destino = "excel_campañas"

if not os.path.exists(carpeta_destino):
    os.makedirs(carpeta_destino)

with SessionLocal() as session:
    result = session.execute(sql_text("SELECT campaign, commercial_services, residential_services, language FROM campaign"))
    rows = result.fetchall()

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
    if "Picture Url 1" not in headers:
        headers.append("Picture Url 1")
        ws.cell(row=1, column=len(headers)).value = "Picture Url 1"
    if "Time" not in headers:
        headers.append("Time")
        ws.cell(row=1, column=len(headers)).value = "Time"

    idx_text = headers.index("Text") + 1
    idx_date = headers.index("Date") + 1
    idx_title = headers.index("Document title") + 1
    idx_yt_title = headers.index("Youtube Video Title") + 1
    idx_yt_tags = headers.index("Youtube Video Tags") + 1
    idx_comment = headers.index("First Comment Text") + 1
    idx_tiktok = headers.index("TikTok Title") + 1
    idx_picture = headers.index("Picture Url 1") + 1
    idx_time = headers.index("Time") + 1

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
                "TikTok Title": gpt.tikTok_title_osceola(theme, 50)
            }

        elif campaign_key == "quick_cleaning":
            theme = gpt.theme_quick_cleaning()
            data = {
                "Text": gpt.copy_quick_cleaning(theme, 100),
                "Document title": gpt.document_title_quick_cleaning(theme),
                "Youtube Video Title": gpt.youtube_video_title_quick_cleaning(theme),
                "Youtube Video Tags": gpt.youtube_video_tags_quick_cleaning(theme),
                "First Comment Text": gpt.firts_comment_quick_cleaning(theme, 50),
                "TikTok Title": gpt.tikTok_title_quick_cleaning(theme, 50)
            }

        elif campaign_key == "elite_chicago_spa":
            theme = gpt.theme_elite_spa()
            data = {
                "Text": gpt.copy_elite_spa(theme, 100),
                "Document title": gpt.document_title_elite_spa(theme),
                "Youtube Video Title": gpt.youtube_video_title_elite_spa(theme),
                "Youtube Video Tags": gpt.youtube_video_tags_elite_spa(theme),
                "First Comment Text": gpt.firts_comment_elite_spa(theme, 50),
                "TikTok Title": gpt.tikTok_title_elite_spa(theme, 50)
            }

        elif campaign_key == "lopez_&_lopez_abogados":
            theme = gpt.theme_lopez_abogados()
            data = {
                "Text": gpt.copy_lopez_abogados(theme, 100),
                "Document title": gpt.document_title_lopez_abogados(theme),
                "Youtube Video Title": gpt.youtube_video_title_lopez_abogados(theme),
                "Youtube Video Tags": gpt.youtube_video_tags_lopez_abogados(theme),
                "First Comment Text": gpt.firts_comment_lopez_abogados(theme, 50),
                "TikTok Title": gpt.tikTok_title_lopez_abogados(theme, 50)
            }

        elif campaign_key.startswith("botanica"):
            theme = gpt.theme_botanica()
            data = {
                "Text": gpt.copy_botanica(theme, 100),
                "Document title": gpt.document_title_botanica(theme),
                "Youtube Video Title": gpt.youtube_video_title_botanica(theme, 50),
                "Youtube Video Tags": gpt.youtube_video_tags_botanica(theme),
                "First Comment Text": gpt.firts_comment_botanica(theme, 50),
                "TikTok Title": gpt.tikTok_title_botanica(theme, 50)
            }

        else:
            print(f"⚠️ Campaña '{campaign_key}' no tiene métodos aún.")
            continue

        print("📥 Texto (Text):", data["Text"])
        print("📄 Título:", data["Document title"])
        plataforma = random.choice(["youtube", "youtube shorts", "instagram reels"])

        try:
            print("🚀 Ejecutando bot 1...")
            subprocess.run(
                ["python", "main.py", data["Text"], plataforma, data["Document title"], campaign_key],
                cwd=r"C:\\Users\\DESARROLLADOR\\Documents\\Manuel Cardona\\bot_creacion_reels",
                check=True,
                timeout=900
            )
        except subprocess.CalledProcessError as e:
            print(f"❌ Error al ejecutar bot 1: {e}")
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

        if not resultados:
            print(f"⚠️ No se encontraron resultados para {campaign_key} en la DB.")
        else:
            for i, fila_db in enumerate(resultados):
                descripcion, plataforma, url = fila_db
                fecha_reel = fecha_actual + timedelta(days=i)
                dia_nombre = dias_semana[fecha_reel.weekday()]

                # Obtener horario aleatorio desde tabla horarios
                horario_query = sql_text("""
                    SELECT hour FROM horarios 
                    WHERE platform_video = :plat AND day = :dia
                """)
                horarios = session.execute(horario_query, {"plat": plataforma, "dia": dia_nombre}).fetchall()
                id_horario = None
                hora_final = "00:00"

                if horarios:
                    horario_elegido = random.choice(horarios)
                    hora_final = horario_elegido[0].strftime("%H:%M")
                    
                    # Obtener el id de ese horario específico
                    id_horario_query = sql_text("""
                        SELECT id FROM horarios
                        WHERE platform_video = :plat AND day = :dia AND hour = :hora
                        LIMIT 1
                    """)
                    resultado = session.execute(id_horario_query, {
                        "plat": plataforma,
                        "dia": dia_nombre,
                        "hora": horario_elegido[0]
                    }).fetchone()
                    
                    if resultado:
                        id_horario = resultado[0]


                for row in range(2, ws.max_row + 1):
                    if not ws.cell(row=row, column=idx_text).value:
                        ws.cell(row=row, column=idx_text).value = descripcion
                        ws.cell(row=row, column=idx_date).value = fecha_reel.strftime("%d/%m/%Y")
                        ws.cell(row=row, column=idx_title).value = ""
                        ws.cell(row=row, column=idx_yt_title).value = ""
                        ws.cell(row=row, column=idx_yt_tags).value = ""
                        ws.cell(row=row, column=idx_comment).value = ""
                        ws.cell(row=row, column=idx_tiktok).value = ""
                        ws.cell(row=row, column=idx_picture).value = url
                        ws.cell(row=row, column=idx_time).value = hora_final
                        print(f"✅ Fila {row} completada en plantilla.")
                        # Asignar id_horario a la tabla videos
                        if id_horario:
                            campaign_key = str(campaign_key)
                            descripcion = str(descripcion)
                            update_query = sql_text("""
                                UPDATE videos
                                SET id_horario = :id_hor
                                WHERE ctid = (
                                    SELECT ctid FROM videos
                                    WHERE campaign = :camp AND description = :desc AND upload_drive = true
                                    LIMIT 1
                                )
                            """)
                            session.execute(update_query, {
                                "id_hor": int(id_horario),
                                "camp": str(campaign_key),
                                "desc": str(descripcion)
                            })
                            session.commit()
                        break

            wb.save(excel_path)
            print(f"📊 Excel final guardado: {excel_path}")

print("\n✅ Todas las campañas han sido procesadas.")