from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List, Dict, Any

# --- RECETA ---
class MedicamentoItem(BaseModel):
    nombre: str
    dosis: str
    frecuencia: str

class RecetaCreate(BaseModel):
    id_medico: int
    id_cliente: int
    detalle_medicamentos: List[MedicamentoItem] # Validamos que sea una lista correcta

class RecetaResponse(RecetaCreate):
    id: int
    fecha_emision: datetime
    archivo_url: Optional[str]

    class Config:
        from_attributes = True

# --- HISTORIA CLÍNICA ---
class HistoriaClinicaCreate(BaseModel):
    id_medico: int
    id_cliente: int
    id_turno: Optional[int]
    motivo_consulta: str
    observaciones: str
    diagnostico: Optional[str]
    tratamiento: Optional[str]
    
    # Aquí validamos que signoss vitales sea un diccionario
    signos_vitales: Optional[Dict[str, Any]] 

class HistoriaClinicaResponse(HistoriaClinicaCreate):
    id: int
    created_at: datetime
    archivos_adjuntos: Optional[List[str]]

    class Config:
        from_attributes = True