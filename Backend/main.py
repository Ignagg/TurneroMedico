from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import engine, Base

# Importamos los routers (los pasillos del hotel)
from routes import pacientes

# Inicializa las tablas si no existen (útil como seguridad)
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Sistema Médico API",
    description="Backend para gestión de turnos y recetas",
    version="1.0.0"
)

# --- CONFIGURACIÓN CORS ---
# Permite que tu Frontend (React/Vite) hable con este Backend
origins = [
    "http://localhost:5173", # Puerto por defecto de Vite
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"], # Permite GET, POST, PUT, DELETE, etc.
    allow_headers=["*"],
)

# --- ENCHUFAR ROUTERS ---
# Todo lo que esté en pacientes.py tendrá el prefijo /pacientes
# Ej: la ruta final será: POST http://localhost:8000/pacientes/perfil
app.include_router(pacientes.router, prefix="/pacientes", tags=["Pacientes"])

@app.get("/")
def health_check():
    return {"status": "ok", "message": "La API está corriendo correctamente 🚀"}