# Sistema de Gestión de Horarios

Este proyecto es una aplicación web desarrollada en Django que permite gestionar los horarios de los empleados en diferentes locales. Los usuarios con permisos adecuados pueden crear, modificar y listar horarios, así como manejar la información de los locales y empleados.

## Características

- **Gestión de Locales**: Permite crear y listar locales.
- **Gestión de Empleados**: Permite crear y listar empleados, asignándolos a locales específicos.
- **Asignación de Horarios**: Los usuarios pueden asignar horarios a los empleados, especificando la hora de inicio, la hora de fin y la fecha.
- **Listar Horarios**: Permite ver todos los horarios asignados.

## Requisitos

- Python 3.x
- Django 5.x

## Instalación

1. **Clona el repositorio**:

   ```bash
   git clone https://github.com/tu_usuario/tu_repositorio.git
   cd tu_repositorio

2. Crea un entorno virtual:

bash
Copiar código
python -m venv venv

3. Activa el entorno virtual:

En Windows:

bash
Copiar código
venv\Scripts\activate

En macOS/Linux:

bash
Copiar código
source venv/bin/activate

4. Instala las dependencias:

bash
Copiar código
pip install django

5. Realiza las migraciones de la base de datos:

bash
Copiar código
python manage.py migrate

6. Crea un superusuario para acceder al panel administrativo:

bash
Copiar código
python manage.py createsuperuser
Inicia el servidor de desarrollo:

bash
Copiar código
python manage.py runserver

6.Accede a la aplicación: Abre tu navegador y ve a http://127.0.0.1:8000/.

Uso

Ingreso al Sistema

Los usuarios deben iniciar sesión para acceder a las funcionalidades de la aplicación. Solo los usuarios con permisos adecuados pueden gestionar locales, empleados y horarios.

Funcionalidades

Crear Local: Accede a la sección de creación de locales para añadir nuevos locales al sistema.
Listar Locales: Visualiza todos los locales existentes.
Crear Empleado: Añade nuevos empleados y asígnalos a un local.
Listar Empleados: Visualiza todos los empleados registrados.
Asignar Horarios: Selecciona un local y un empleado, y asigna horarios específicos.
Listar Horarios: Visualiza todos los horarios asignados a los empleados.

Estructura del Proyecto
app_check/: Contiene la lógica principal de la aplicación.
models.py: Define los modelos de datos (Local, Empleado, Horario).
views.py: Contiene las vistas que gestionan la lógica de la aplicación.
forms.py: Define los formularios utilizados en la aplicación.
templates/: Contiene las plantillas HTML para renderizar las vistas.

Contribuciones
Las contribuciones son bienvenidas. Si deseas contribuir a este proyecto, por favor abre un issue o envía un pull request.

Caso de Prueba 1: Creación de Locales

Objetivo: Verificar que se puede crear un nuevo local correctamente.

Precondiciones:

El usuario debe estar autenticado con permisos de RRHH.

Pasos:

Iniciar sesión en la aplicación como un usuario con permisos de RRHH.

Navegar a la sección de "Crear Local".

Completar el formulario con un nombre válido para el nuevo local.

Hacer clic en el botón "Crear".

Resultados Esperados:

El local debe ser creado y guardado en la base de datos.

El usuario debe ser redirigido a la página de lista de locales.

En la lista de locales, debe aparecer el nuevo local creado.

Caso de Prueba 2: Asignación de Horarios

Objetivo: Verificar que se puede asignar un horario a un empleado correctamente.

Precondiciones:

Debe existir al menos un local y un empleado en la base de datos.

El usuario debe estar autenticado con permisos de RRHH.

Pasos:

Iniciar sesión en la aplicación como un usuario con permisos de RRHH.

Navegar a la sección de "Asignar Horarios".

Seleccionar un local del menú desplegable.

Seleccionar un empleado del menú desplegable.

Completar el formulario con una hora de inicio, hora de fin y una fecha válida.

Hacer clic en el botón "Asignar Horario".

Resultados Esperados:

El horario debe ser asignado y guardado en la base de datos.

El usuario debe ser redirigido a la página de lista de horarios.

En la lista de horarios, debe aparecer el nuevo horario asignado con la información correcta.

Caso de Prueba 3: Listado de Horarios

Objetivo: Verificar que se muestran todos los horarios asignados en la lista de horarios.

Precondiciones:

Debe haber al menos un horario asignado en la base de datos.

El usuario debe estar autenticado con permisos de RRHH.

Pasos:

Iniciar sesión en la aplicación como un usuario con permisos de RRHH.

Navegar a la sección de "Lista de Horarios".

Resultados Esperados:

Se debe mostrar una lista de todos los horarios asignados.

Cada entrada en la lista debe mostrar el empleado, el local, la fecha, la hora de inicio y la hora de fin.

La lista debe reflejar cualquier cambio reciente en la base de datos (si se asignaron nuevos horarios antes de la prueba).

Consideraciones Adicionales

Pruebas de Datos Válidos/Inválidos: Puedes ampliar los casos de prueba incluyendo intentos de creación de locales o asignación de horarios con datos inválidos (por ejemplo, horas de fin anteriores a las horas de inicio).

Interfaz de Usuario: Verificar que los mensajes de éxito o error se muestren correctamente.

Pruebas de Seguridad: Asegúrate de que los usuarios sin permisos no puedan acceder a las funciones restringidas.
