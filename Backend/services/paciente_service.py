from sqlalchemy.orm import Session
from fastapi import HTTPException
from models.users import Cliente
from schemas.paciente_schemas import ClienteCreate
from repositories.paciente_repository import PacienteRepository
import uuid

class PacienteService:
    def __init__(self, db: Session):
        self.db = db
        self.repo = PacienteRepository()

    def crear_perfil(self, datos: ClienteCreate, user_id: str):
        # 0. Convertir el ID de string a UUID (Postgres lo requiere)
        try:
            uid_obj = uuid.UUID(user_id)
        except ValueError:
            raise HTTPException(status_code=400, detail="ID de usuario inválido")

        # 1. Validar duplicados de Usuario
        # (Un usuario no puede tener dos perfiles de paciente)
        if self.repo.get_by_user_id(self.db, uid_obj):
            raise HTTPException(status_code=400, detail="Este usuario ya tiene un perfil de paciente creado.")

        # 2. Validar duplicados de DNI
        if self.repo.get_by_dni(self.db, datos.dni):
            raise HTTPException(status_code=400, detail="El DNI ya existe en el sistema.")
        
        # 3. Convertir Schema a Modelo (Mapeo)
        nuevo_cliente = Cliente(
            id_usuario=uid_obj, 
            nombre=datos.nombre,
            apellido=datos.apellido,
            dni=datos.dni,
            fecha_nacimiento=datos.fecha_nacimiento,
            telefono=datos.telefono,
            numero_afiliado=datos.numero_afiliado,
            id_plan=datos.id_plan
        )
        
        # 4. Guardar usando el repositorio
        return self.repo.create(self.db, nuevo_cliente)