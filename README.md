# 📌 Django CRUD Application

Este es un proyecto de CRUD (Create, Read, Update, Delete) desarrollado con Django. Permite gestionar registros de una base de datos de manera sencilla a través de una interfaz web dirigido a los riferos.

# 🚀 Tecnologías utilizadas

Django (Framework backend)
SQLite (Base de datos por defecto, pero puedes cambiarla)
Bootstrap (Para mejorar la interfaz)
DataTables (Para la paginación y búsqueda en listas)
📂 Estructura del Proyecto
bash
Copiar
Editar

```info / django_crud
│── /clientes/ # Aplicación principal
│ ├── migrations/ # Migraciones de la base de datos
│ ├── static/ # Archivos estáticos (CSS, JS, imágenes)
│ ├── templates/ # Plantillas HTML
│ ├── views.py # Lógica de las vistas
│ ├── models.py # Modelos de la base de datos
│ ├── urls.py # Rutas de la aplicación
│── /django_crud/ # Configuración global del proyecto
│ ├── settings.py # Configuración de Django
│ ├── urls.py # Rutas principales del proyecto
│── db.sqlite3 # Base de datos (puede cambiarse a PostgreSQL, MySQL, etc.)
│── manage.py # Script de gestión de Django
│── requirements.txt # Dependencias del proyecto
│── README.md # Documentación del proyecto
⚙️ Instalación y Configuración
### 1️⃣ Clonar el repositorio
bash
Copiar
Editar
git clone https://github.com/tu-usuario/django-crud.git
cd django-crud
### 2️⃣ Crear un entorno virtual e instalar dependencias
bash
Copiar
Editar
python -m venv venv
source venv/bin/activate # En Windows: venv\Scripts\activate
pip install -r requirements.txt
### 3️⃣ Aplicar migraciones
bash
Copiar
Editar
python manage.py migrate
### 4️⃣ Crear un superusuario (opcional)
bash
Copiar
Editar
python manage.py createsuperuser
Accederás al panel de administración en: http://127.0.0.1:8000/admin/

### 5️⃣ Ejecutar el servidor
bash
Copiar
Editar
python manage.py runserver
Accede a http://127.0.0.1:8000/ en tu navegador.

## 🛠️ Funcionalidades
✔️ Crear nuevos registros
✔️ Listar los registros en una tabla con paginación
✔️ Buscar y filtrar información con DataTables
✔️ Actualizar registros existentes
✔️ Eliminar registros con confirmación

## 📌 Rutas Principales
/ → Página principal con la lista de registros
/crear/ → Formulario para añadir nuevos datos
/editar/<id>/ → Modificar un registro
/eliminar/<id>/ → Eliminar un registro
📜 Licencia
Este proyecto está bajo la licencia MIT, por lo que puedes modificarlo y distribuirlo libremente.
```
