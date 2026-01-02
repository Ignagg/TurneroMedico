from sqlalchemy import Column, Integer, String, ForeignKey, Numeric, DateTime
from sqlalchemy.orm import relationship
from database import Base

# --- ESPECIALIDAD ---
class Especialidad(Base):
    __tablename__ = "Especialidad"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, unique=True, nullable=False)
    descripcion = Column(String)

    medicos = relationship("Medico", back_populates="especialidad")

# --- OBRA SOCIAL ---
class ObraSocial(Base):
    __tablename__ = "ObraSocial"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, unique=True, nullable=False)
    
    planes = relationship("Plan", back_populates="obra_social")

# --- PLAN ---
class Plan(Base):
    __tablename__ = "Plan"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    id_obra_social = Column(Integer, ForeignKey("ObraSocial.id"))

    obra_social = relationship("ObraSocial", back_populates="planes")
    clientes = relationship("Cliente", back_populates="plan") # Viene de users.py
    coberturas = relationship("Cobertura", back_populates="plan")

# --- PRESTACIÓN ---
class Prestacion(Base):
    __tablename__ = "Prestacion"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    precio_base = Column(Numeric(10, 2), nullable=False)

    coberturas = relationship("Cobertura", back_populates="prestacion")
    turnos = relationship("Turno", back_populates="prestacion")

# --- COBERTURA ---
class Cobertura(Base):
    __tablename__ = "Cobertura"
    id = Column(Integer, primary_key=True, index=True)
    id_plan = Column(Integer, ForeignKey("Plan.id"))
    id_prestacion = Column(Integer, ForeignKey("Prestacion.id"))
    porcentaje_cobertura = Column(Integer, nullable=False)
    monto_coseguro = Column(Numeric(10, 2), default=0)

    plan = relationship("Plan", back_populates="coberturas")
    prestacion = relationship("Prestacion", back_populates="coberturas")