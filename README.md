# TurneroMedico

## Tecnologias:
### FastAPI
### React
### Vite
### SQLAlchemy
### Tailwind


Markdown

## 🛠️ Guía de Instalación y Ejecución

Sigue estos pasos para levantar el proyecto en tu entorno local.

### 1. Prerrequisitos (Lo que necesitas tener instalado)

Antes de empezar, asegúrate de tener instalado lo siguiente en tu sistema operativo:

* **Git:** Para clonar el repositorio.
* **Editor de Código:** Recomendado [VS Code](https://code.visualstudio.com/).
* **Backend:**
    * [Python 3.10+](https://www.python.org/) (o Java/Node según tu caso).
    * Gestor de paquetes (pip o maven).
* **Frontend:**
    * [Node.js](https://nodejs.org/) (Versión LTS v18+ recomendada).
    * npm (viene con Node) o pnpm.
* **Base de Datos:**
    * [Docker Desktop](https://www.docker.com/) (Recomendado para levantar la BD fácilmente).
    * *Opcional:* Si no usas Docker, tener instalado el motor de base de datos localmente (ej. PostgreSQL, MySQL).

---

### 2. Configuración Inicial

#### A. Clonar el repositorio
"bash
git clone <URL_DEL_REPOSITORIO>
cd <NOMBRE_DE_LA_CARPETA>"

#### B. Configuración del Backend (Servidor)
Navega a la carpeta del backend: cd backend

Crea un entorno virtual (recomendado para Python): python -m venv venv

Activa el entorno virtual:

Windows: .\venv\Scripts\activate

Mac/Linux: source venv/bin/activate

Instala las dependencias: pip install -r requirements.txt

Variables de Entorno: Crea un archivo .env basado en el .env.example y configura tus credenciales de base de datos.

#### C. Configuración del Frontend (Cliente)
Abre una nueva terminal y navega a la carpeta del frontend: cd frontend

Instala las librerías de Node: npm install

### 3. Ejecución del Proyecto (Cómo levantar todo)
Para que el sistema funcione, necesitas tener 3 cosas corriendo simultáneamente:

Shutterstock

Paso 1: Levantar la Base de Datos
Si usas Docker, corre el siguiente comando en la raíz del proyecto:

Bash

docker-compose up -d
Si usas instalación local, asegúrate de que el servicio (Postgres/MySQL) esté activo en tus servicios de Windows/Linux.

Paso 2: Levantar el Backend (API)
En la terminal donde configuraste el Backend (con el entorno virtual activo):

Bash

# Ejemplo para FastAPI / Uvicorn
uvicorn main:app --reload
Debería indicar que está corriendo en http://localhost:8000 (o el puerto que uses).

Paso 3: Levantar el Frontend (Web)
En la terminal del Frontend:

Bash

npm run dev
Debería indicar que está corriendo en http://localhost:5173 (Vite) o 3000.

⚠️ Aclaraciones Importantes
Terminales Abiertas: Necesitas mantener abiertas las terminales del Backend y del Frontend. Si cierras alguna, esa parte del sistema dejará de funcionar.

CORS: Si el frontend no conecta con el backend, verifica que el CORS en el backend esté configurado para aceptar peticiones desde el puerto de tu frontend.

Datos de prueba: Si la base de datos está vacía, recuerda correr el script de "seed" o migración para poblarla con datos iniciales: python seed_data.py (ajustar según tu proyecto).


---

### Explicación de los puntos clave para ti (El Desarrollador)

Para que tengas claro el porqué de cada sección:

1.  **Terminales Simultáneas:** Es el error más común. Aclara siempre que necesitan **dos consolas distintas** (una para Python/Java y otra para Node/React). No pueden correr en la misma línea de comandos a menos que usen herramientas avanzadas.
2.  **El archivo `.env`:** Nunca subas tu archivo `.env` real al repositorio (por seguridad). Sube un `.env.example` con los nombres de las variables vacíos para que quien descargue el proyecto sepa qué llenar.
3.  **Docker vs. Local:** Si usas Docker para la base de datos, es mucho más fácil para quien corrige el trabajo, ya que no tiene que instalar PostgreSQL/MySQL en su PC, solo Docker.

**¿Te gustaría que personalice los comandos de instalación para una tecnología específica (ej. FastAPI vs Flask o React vs Angular)?**
