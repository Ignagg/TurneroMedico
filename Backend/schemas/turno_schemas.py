from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List

# Input: Para pedir un turno
class TurnoCreate(BaseModel):
    fecha_hora_inicio: datetime
    id_medico: int
    id_prestacion: int # Qué se va a hacer

# Output: Para mostrar el turno en pantalla
class TurnoResponse(BaseModel):
    id: int
    fecha_hora_inicio: datetime
    fecha_hora_fin: datetime
    estado: str
    
    # Aquí puedes anidar otros schemas si quieres mostrar info detallada
    # (Por ahora devolvemos solo IDs para no complicarla)
    id_medico: int
    id_cliente: Optional[int]
    
    class Config:
        from_attributes = True