from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from dotenv import load_dotenv

# 1. Cargar las variables del archivo .env
load_dotenv()

# 2. Obtener la URL de conexión
# Si no encuentra la variable, tira error (mejor que fallar en silencio)
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")

if not SQLALCHEMY_DATABASE_URL:
    raise ValueError("❌ Error: No se encontró DATABASE_URL en el archivo .env")

# 3. Crear el "Motor" (Engine)
# Nota: Si usas SQLite se necesita un argumento extra, pero para Postgres esto está perfecto.
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# 4. Crear la fábrica de Sesiones
# Cada petición (request) tendrá su propia sesión de base de datos
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 5. La Clase Base para tus Modelos
# Todos tus modelos (User, Medico, etc.) heredarán de esta clase
Base = declarative_base()

# 6. Dependencia para inyectar la DB en los endpoints
# Esto se usa en los routers: def endpoint(db: Session = Depends(get_db)):
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()