🛠️ Motorcycle Workshop API - FastAPI Backend
=============================================

Este proyecto es una API REST desarrollada con **FastAPI** para gestionar un sistema de taller mecánico de motocicletas. Está diseñada para interactuar con un sistema frontend y proporciona operaciones completas sobre clientes, motocicletas y órdenes de servicio.

* * *

🚀 Características principales
------------------------------

*   📄 **CRUD completo** para:
    *   Clientes
    *   Motocicletas (relacionadas con clientes)
    *   Órdenes de Servicio (relacionadas con motocicletas)
*   🧾 **Órdenes de servicio**:
    *   Captura de diagnóstico
    *   Registro de kilometraje
    *   Lista de servicios realizados (nombre y precio)
    *   Cálculo automático de:
        *   Subtotal
        *   IVA (16%)
        *   Total

* * *

⚙️ Configuración del entorno
----------------------------

### 1\. Clonar el repositorio

    git clone https://github.com/isauraplata/Api-rest-motocicletas.git
    

### 2\. Crear y activar entorno virtual

    python -m venv venv
    
    # En Windows
    venv\Scripts\activate
    
    # En macOS/Linux
    source venv/bin/activate
    

### 3\. Instalar dependencias

    pip install -r requirements.txt
    

### 4\. Configurar variables de entorno

Crea un archivo `.env` en la raíz del proyecto, reemplaza con tus credenciales:

    # Database configuration
    DATABASE_URL=mysql+pymysql://user:password@localhost:3306/taller_motociclista
    
    # API configuration
    API_V1_STR=/api/v1
    PROJECT_NAME=Motorcycle API
    
    # Security
    SECRET_KEY=your-super-secret-key
    ALGORITHM=HS256
    ACCESS_TOKEN_EXPIRE_MINUTES=30
    
    # Tax settings
    TAX_RATE=0.16
    

### 5\. Iniciar el servidor de desarrollo
Debes entrar al directorio src, y al levantar la API con el siguiente comando, se crearán automáticamente las tablas en la base de datos

```bash
cd src/
uvicorn main:app --reload
```
    

### 6\. La documentación de la API REST, generada con Swagger UI, está disponible en:

    http://localhost:8000/api/v1/docs
