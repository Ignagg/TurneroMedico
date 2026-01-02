from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Numeric
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID # Necesario para los IDs de Supabase
import uuid
from database import Base

# --- ROL ---
class Rol(Base):
    __tablename__ = "Rol" # Debe ser IGUAL al nombre en SQL
    
    id = Column(Integer, primary_key=True, index=True)
    nombre_rol = Column(String, unique=True, nullable=False)
    descripcion = Column(String)

    # Relación inversa (opcional, para acceder desde Rol a sus usuarios)
    users = relationship("User", back_populates="rol")

# --- USER (Vinculado a Supabase Auth) ---
class User(Base):
    __tablename__ = "Users"

    id = Column(UUID(as_uuid=True), primary_key=True) # UUID exacto
    email = Column(String, unique=True, nullable=False)
    username = Column(String, unique=True)
    id_role = Column(Integer, ForeignKey("Rol.id"))

    rol = relationship("Rol", back_populates="users")
    
    # Relaciones 1 a 1
    cliente_perfil = relationship("Cliente", back_populates="usuario", uselist=False)
    medico_perfil = relationship("Medico", back_populates="usuario", uselist=False)

# --- CLIENTE ---
class Cliente(Base):
    __tablename__ = "Cliente"

    id = Column(Integer, primary_key=True, index=True)
    id_usuario = Column(UUID(as_uuid=True), ForeignKey("Users.id"), unique=True)
    nombre = Column(String, nullable=False)
    apellido = Column(String, nullable=False)
    dni = Column(String, unique=True, nullable=False)
    fecha_nacimiento = Column(DateTime)
    telefono = Column(String)
    id_plan = Column(Integer, ForeignKey("Plan.id")) # Ojo: Plan está en otro archivo, pero SQL lo resuelve
    numero_afiliado = Column(String)

    usuario = relationship("User", back_populates="cliente_perfil")
    plan = relationship("Plan", back_populates="clientes") # Necesitaremos definir esto en Plan
    turnos = relationship("Turno", back_populates="cliente")

# --- MÉDICO ---
class Medico(Base):
    __tablename__ = "Medico"

    id = Column(Integer, primary_key=True, index=True)
    id_usuario = Column(UUID(as_uuid=True), ForeignKey("Users.id"), unique=True)
    matricula = Column(String, unique=True, nullable=False)
    id_especialidad = Column(Integer, ForeignKey("Especialidad.id")) 
    precio_consulta = Column(Numeric(10, 2), nullable=False)

    usuario = relationship("User", back_populates="medico_perfil")
    especialidad = relationship("Especialidad", back_populates="medicos")
    turnos = relationship("Turno", back_populates="medico")