from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from schemas.paciente_schemas import ClienteCreate, ClienteResponse
from services.paciente_service import PacienteService

router = APIRouter()

@router.post("/perfil", response_model=ClienteResponse)
def crear_perfil_paciente(datos: ClienteCreate, db: Session = Depends(get_db)):
    """
    Endpoint para completar el perfil del paciente.
    """
    
    # --- ZONA DE PRUEBA MANUAL ---
    # 1. Ve a Supabase -> Authentication -> Users.
    # 2. Copia el "User UID" de un usuario que hayas creado.
    # 3. Pégalo aquí abajo entre comillas.
    user_id_hardcodeado = "fe05b97b-8025-4676-90b4-2499bc80c0f6" 
    # Ejemplo: "a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11"
    
    # Validamos que hayas pegado algo
    if user_id_hardcodeado == "PEGAR_TU_UUID_AQUI_REEMPLAZAME":
        raise HTTPException(status_code=500, detail="¡Falta poner el UUID de prueba en el código!")

    # Instanciamos el servicio y ejecutamos la lógica
    service = PacienteService(db)
    result = service.crear_perfil(datos, user_id_hardcodeado)
    
    return result