from pydantic import BaseModel
from datetime import datetime, date
from typing import Optional
from uuid import UUID

# 1. Base: Datos comunes (para no repetir código)
class ClienteBase(BaseModel):
    nombre: str
    apellido: str
    dni: str
    telefono: Optional[str] = None
    numero_afiliado: Optional[str] = None
    fecha_nacimiento: Optional[datetime] = None

# 2. Input: Lo que te manda React para crear el perfil
class ClienteCreate(ClienteBase):
    id_plan: Optional[int] = None # Puede ser null si es particular

# 3. Output: Lo que le devuelves a React (incluye el ID generado)
class ClienteResponse(ClienteBase):
    id: int
    id_usuario: UUID
    id_plan: Optional[int]
    
    # IMPORTANTE: Esto permite que Pydantic lea datos de SQLAlchemy
    class Config:
        from_attributes = True