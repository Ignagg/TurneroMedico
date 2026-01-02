# 🏥 TurneroMedico - Sistema de Gestión de Turnos Clínicos

Sistema integral para la gestión de clínicas, permitiendo la administración de pacientes, médicos, turnos, historias clínicas y recetas digitales.

## 🚀 Tecnologías Utilizadas

### Backend (API)
* **Lenguaje:** Python 3.11+
* **Framework:** FastAPI (Alto rendimiento y validación automática)
* **ORM:** SQLAlchemy (Gestión de Base de Datos)
* **Validación:** Pydantic (Schemas)
* **Generación de Archivos:** ReportLab (Recetas PDF)

### Frontend (Cliente)
* **Framework:** React
* **Build Tool:** Vite (Rápido y ligero)
* **Estilos:** Tailwind CSS
* **HTTP Client:** Axios / Fetch

### Infraestructura & Datos
* **Base de Datos:** PostgreSQL (vía Supabase)
* **Auth & Storage:** Supabase Local
* **Contenedores:** Docker (para orquestar Supabase)

---

## 🏗️ Arquitectura del Backend

El proyecto sigue una arquitectura en capas (Layered Architecture) para garantizar escalabilidad y orden.

```text
backend/
├── main.py                # Punto de entrada. Configura CORS y Rutas.
├── database.py            # Configuración de conexión a PostgreSQL.
├── models/                # (ORM) Espejo de las tablas de la BD (SQLAlchemy).
├── schemas/               # (DTOs) Reglas de validación de entrada/salida (Pydantic).
├── repositories/          # (Data Access) Solo habla con la BD. Sin lógica de negocio.
├── services/              # (Business Logic) Toma decisiones y valida reglas de negocio.
└── routers/               # (Controllers) Recibe peticiones HTTP y responde al cliente.

🛠️ Guía de Instalación y Ejecución
Sigue estos pasos para levantar el entorno de desarrollo completo.

1. Prerrequisitos
Asegúrate de tener instalado:

Docker Desktop (Indispensable para Supabase).

Python 3.10+.

Node.js v18+.

Git.

2. Levantar la Infraestructura (Supabase)
No necesitas instalar PostgreSQL manualmente. Docker lo hace por ti.

Abre Docker Desktop.

En la terminal raíz del proyecto:

Bash

npx supabase start
Nota: Copia la DB URL y la Service_role key que aparecen al finalizar, las necesitarás para el .env.

Accede al panel visual en: http://127.0.0.1:54323.

3. Configurar y Correr el Backend
Navega a la carpeta:

Bash

cd backend
Crea y activa el entorno virtual:

Bash

python -m venv venv
# Windows:
.\venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate
Instala las dependencias:

Bash

pip install -r requirements.txt
Configura las variables de entorno:

Crea un archivo .env (basado en .env.example).

Pega tu DATABASE_URL (Ej: postgresql://postgres:postgres@127.0.0.1:54322/postgres).

Importante: Asegúrate de usar el puerto correcto (suele ser 54322 en Supabase local).

Inicia el servidor:

Bash

python -m uvicorn main:app --reload
API disponible en: http://127.0.0.1:8000/docs

4. Configurar y Correr el Frontend
Abre una nueva terminal y navega a:

Bash

cd frontend
Instala las librerías:

Bash

npm install
Inicia la aplicación:

Bash

npm run dev
Web disponible en: http://127.0.0.1:5173

🧪 Testing Manual (Swagger UI)
FastAPI genera documentación automática.

Con el backend corriendo, ve a http://127.0.0.1:8000/docs.

Prueba los endpoints (ej: /pacientes/perfil) directamente desde el navegador.

⚠️ Solución de Problemas Comunes
Error: uvicorn not found:

Asegúrate de tener el entorno virtual activo ((venv) al inicio de la línea de comandos).

Prueba ejecutar: python -m uvicorn main:app --reload.

Error de conexión a BD:

Verifica que Docker esté corriendo.

Revisa que el puerto en el .env coincida con el que muestra npx supabase status.

Error de validación UUID:

Asegúrate de enviar IDs válidos copiados desde el panel de Supabase Authentication.
