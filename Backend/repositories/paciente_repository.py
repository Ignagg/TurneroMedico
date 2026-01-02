from sqlalchemy.orm import Session
from models.users import Cliente
from uuid import UUID

class PacienteRepository:
    def get_by_dni(self, db: Session, dni: str):
        """Busca un paciente por su DNI exacto."""
        return db.query(Cliente).filter(Cliente.dni == dni).first()

    def get_by_user_id(self, db: Session, user_id: UUID):
        """
        Busca el perfil de paciente asociado a un usuario de Supabase.
        Útil para saber si el usuario logueado ya completó su registro.
        """
        return db.query(Cliente).filter(Cliente.id_usuario == user_id).first()

    def create(self, db: Session, paciente: Cliente):
        """
        Guarda un nuevo paciente en la base de datos.
        Recibe una instancia del Modelo (no del Schema).
        """
        db.add(paciente)
        db.commit()
        db.refresh(paciente) # Actualiza el objeto con el ID generado por la BD
        return paciente