# fastApi.py

from contextlib import redirect_stdout
import io
import threading
from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import StreamingResponse
from sqlalchemy import text as sql_text
from fastapi.middleware.cors import CORSMiddleware
from config import SessionLocal
import pandas as pd

from main import run_bot

app = FastAPI()

origins = [
    "http://localhost:3000",  # <- el puerto donde corre tu frontend
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # ✅ Solo permitimos localhost:5173
    allow_credentials=True,
    allow_methods=["*"],    # 🔥 Permitir todos los métodos (POST, GET, etc.)
    allow_headers=["*"],    # 🔥 Permitir todos los headers
)

@app.post("/upload-excel")
async def actualizar_excel(file: UploadFile, id_campaign: int = Form(...)):
    try:
        contents = await file.read()
        df = pd.read_excel(io.BytesIO(contents))
        actualizados = 0
        insertados = 0
        eliminados = 0

        with SessionLocal() as session:
            # 🔍 Traer registros actuales
            result = session.execute(sql_text("""
                SELECT id FROM contenido_semanal
                WHERE id_campaign = :id_campaign
                ORDER BY id
            """), {"id_campaign": id_campaign})
            registros = result.fetchall()

            for i, row in enumerate(df.itertuples()):
                dia = str(row[1]).strip() if pd.notna(row[1]) else None
                canal = str(row[2]).strip() if pd.notna(row[2]) else None
                servicio = str(row[3]).strip() if pd.notna(row[3]) else None
                tipo = str(row[4]).strip() if pd.notna(row[4]) else None
                descripcion = str(row[5]).strip() if pd.notna(row[5]) else None
                hashtags = str(row[6]).strip() if pd.notna(row[6]) else None
                sonido_raw = str(row[7]).strip() if pd.notna(row[7]) else None
                sonido = None if sonido_raw == "—" else sonido_raw

                if i < len(registros):
                    # 🔄 Actualizar
                    session.execute(sql_text("""
                        UPDATE contenido_semanal
                        SET dia = :dia,
                            canal = :canal,
                            servicio = :servicio,
                            tipo = :tipo,
                            descripcion = :descripcion,
                            hashtags = :hashtags,
                            sonido = :sonido
                        WHERE id = :id
                    """), {
                        "dia": dia,
                        "canal": canal,
                        "servicio": servicio,
                        "tipo": tipo,
                        "descripcion": descripcion,
                        "hashtags": hashtags,
                        "sonido": sonido,
                        "id": registros[i][0]
                    })
                    actualizados += 1
                else:
                    # ➕ Insertar
                    session.execute(sql_text("""
                        INSERT INTO contenido_semanal (id_campaign, dia, canal, servicio, tipo, descripcion, hashtags, sonido)
                        VALUES (:id_campaign, :dia, :canal, :servicio, :tipo, :descripcion, :hashtags, :sonido)
                    """), {
                        "id_campaign": id_campaign,
                        "dia": dia,
                        "canal": canal,
                        "servicio": servicio,
                        "tipo": tipo,
                        "descripcion": descripcion,
                        "hashtags": hashtags,
                        "sonido": sonido
                    })
                    insertados += 1

            # 🗑️ Eliminar registros sobrantes
            if len(df) < len(registros):
                ids_sobrantes = [r[0] for r in registros[len(df):]]
                # Eliminar registros dependientes en 'videos' primero
                session.execute(sql_text("""
                    DELETE FROM videos
                    WHERE id_contenido IN :ids
                """), {"ids": tuple(ids_sobrantes)})
    
                session.execute(sql_text("""
                    DELETE FROM contenido_semanal
                    WHERE id IN :ids
                """), {"ids": tuple(ids_sobrantes)})
                eliminados = len(ids_sobrantes)

            session.commit()
            return {
                "message": f"✅ Se actualizaron {actualizados}, se insertaron {insertados} y se eliminaron {eliminados} registros para la campaña {id_campaign}."
            }

    except Exception as e:
        return {"error": f"❌ Error al procesar Excel: {e}"}


    
@app.get("/campaigns")
def obtener_campaigns():
    with SessionLocal() as session:
        result = session.execute(sql_text("""
            SELECT id, campaign FROM campaign
        """))
        campaigns = [{"id": r[0], "nombre": r[1]} for r in result.fetchall()]
        return campaigns



@app.get("/api/ejecutar-bot")
async def ejecutar_bot_stream():
    def generar_salida():
        buffer = io.StringIO()
        with redirect_stdout(buffer):
            run_bot()

        buffer.seek(0)
        for line in buffer:
            yield f"data: {line.strip()}\n\n"

    return StreamingResponse(generar_salida(), media_type="text/event-stream")
