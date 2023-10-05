# HASHEO DE CONTRASEÑA

Esta es una aplicación web creada en Flask que incluye archivos Docker para facilitar la creación de la imagen de contenedor y utiliza `migrate` para gestionar las migraciones de la base de datos.

## Requisitos

Asegúrate de tener instalado Python en tu sistema antes de continuar. Además, puedes utilizar [virtualenv](https://virtualenv.pypa.io/en/stable/) para crear un entorno virtual aislado para tu proyecto.

## Instalación

1. Clona este repositorio en tu máquina local:

   ```bash
   git clone https://github.com/tu-usuario/mi-aplicacion-flask.git
Accede al directorio del proyecto:

bash
Copy code
cd mi-aplicacion-flask
Crea un entorno virtual (opcional pero recomendado):

bash
Copy code
python -m venv venv
Activa el entorno virtual (si se creó):

En Windows:

bash
Copy code
venv\Scripts\activate
En macOS y Linux:

bash
Copy code
source venv/bin/activate

## Instala las dependencias desde el archivo requirements.txt:

bash
Copy code
pip install -r requirements.txt
Docker
Para crear la imagen de Docker y ejecutar la aplicación en un contenedor, sigue estos pasos:

Asegúrate de tener Docker instalado en tu sistema.

En el directorio raíz del proyecto, utiliza el siguiente comando para construir la imagen de Docker:

bash
Copy code
docker build -t mi-aplicacion-flask:latest .
Luego, ejecuta el contenedor:

bash
Copy code
docker run -p 5000:5000 mi-aplicacion-flask
La aplicación estará disponible en http://localhost:5000.

Migraciones de la Base de Datos
Este proyecto utiliza migrate para gestionar las migraciones de la base de datos. Asegúrate de configurar tus modelos en la carpeta models. Luego, puedes crear y aplicar migraciones de la siguiente manera:

## Crear una migración inicial:

bash
Copy code
flask db init
Generar una migración a partir de los modelos:

bash
Copy code
flask db migrate -m "Descripción de la migración"
Aplicar la migración a la base de datos:

bash
Copy code
flask db upgrade
Contribuciones
Si deseas contribuir a este proyecto, ¡estamos abiertos a tus sugerencias y contribuciones! Siéntete libre de abrir problemas (issues) y enviar solicitudes de extracción (pull requests).

