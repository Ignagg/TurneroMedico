from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from database import Base

# --- TURNO ---
class Turno(Base):
    __tablename__ = "Turno"

    id = Column(Integer, primary_key=True, index=True)
    fecha_hora_inicio = Column(DateTime, nullable=False)
    fecha_hora_fin = Column(DateTime, nullable=False)
    estado = Column(String, default='Disponible')
    
    id_medico = Column(Integer, ForeignKey("Medico.id"))
    id_cliente = Column(Integer, ForeignKey("Cliente.id"))
    id_prestacion = Column(Integer, ForeignKey("Prestacion.id"))

    # Relaciones para navegar (ej: turno.medico.apellido)
    medico = relationship("Medico", back_populates="turnos")
    cliente = relationship("Cliente", back_populates="turnos")
    prestacion = relationship("Prestacion", back_populates="turnos")
    
    notificaciones = relationship("Notificaciones", back_populates="turno")

# --- NOTIFICACIONES ---
class Notificaciones(Base):
    __tablename__ = "Notificaciones"

    id = Column(Integer, primary_key=True, index=True)
    id_turno = Column(Integer, ForeignKey("Turno.id"))
    fecha_envio = Column(DateTime)
    tipo = Column(String, nullable=False)
    destino = Column(String, nullable=False)
    estado = Column(String, default='Enviado')
    mensaje_error = Column(String)

    turno = relationship("Turno", back_populates="notificaciones")