from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import JSONB, ARRAY # Tipos especiales de Postgres
from database import Base
import datetime

# --- RECETA ---
class Receta(Base):
    __tablename__ = "Receta"

    id = Column(Integer, primary_key=True, index=True)
    id_turno = Column(Integer, ForeignKey("Turno.id"), nullable=True)
    id_medico = Column(Integer, ForeignKey("Medico.id"), nullable=False)
    id_cliente = Column(Integer, ForeignKey("Cliente.id"), nullable=False)
    fecha_emision = Column(DateTime, default=datetime.datetime.utcnow)
    
    archivo_url = Column(String) # Link al PDF en Storage
    
    # Aquí guardamos la lista de medicamentos como un objeto JSON
    # Ej: [{"nombre": "Ibuprofeno", "dosis": "600mg"}, ...]
    detalle_medicamentos = Column(JSONB)

    # Relaciones
    turno = relationship("Turno") # No necesitamos back_populates si no lo vamos a navegar desde Turno
    medico = relationship("Medico")
    cliente = relationship("Cliente")

# --- HISTORIA CLÍNICA ---
class HistoriaClinica(Base):
    __tablename__ = "HistoriaClinica"

    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    
    id_cliente = Column(Integer, ForeignKey("Cliente.id"), nullable=False)
    id_medico = Column(Integer, ForeignKey("Medico.id"), nullable=False)
    id_turno = Column(Integer, ForeignKey("Turno.id"), nullable=True)

    # 1. Subjetivo
    motivo_consulta = Column(Text, nullable=False)

    # 2. Objetivo (Datos estructurados)
    # Ej: {"presion": "120/80", "peso": 75.5, "temperatura": 36}
    signos_vitales = Column(JSONB)

    # 3. Análisis
    observaciones = Column(Text)
    diagnostico = Column(Text)
    tratamiento = Column(Text)

    # 4. Adjuntos (Lista de URLs de imágenes/PDFs)
    # Postgres permite guardar arrays nativos. Ej: ["url1.jpg", "url2.pdf"]
    archivos_adjuntos = Column(ARRAY(String))

    # Relaciones
    cliente = relationship("Cliente") # Podrías poner back_populates="historia_clinica" en Cliente si quisieras
    medico = relationship("Medico")
    turno = relationship("Turno")
