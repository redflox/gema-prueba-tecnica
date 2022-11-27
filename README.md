## Prueba JERRE JERRE

- Tiempo planeado de solución


  Para desarrollar este modulo, bajo mi experiencia en el framework django y python planteo que el tiempo estimado es de 6 horas.

  * * *
- Explicación de su solución
  
  
  He usado Django como framework, el cual me permite manejar archivos, conectame a una base de datos haciendo uso de un ORM, servir contenido estatico y dinamico. 

  Para atacar el problema lo primero fue leer y entender los requerimientos funcionales y no funcionales. De ahi decidi realizar el modelo de base de datos, planteado de la siguiente manera:

  ![Descripción de la imagen](/media/modelo.png)

  Luego de tener el modelo, cree un entorno virtual con VIRTUALENV para asi manejar las dependecias del proyecto de manera aislada.

  Con el entorno virtual activo, procedo a instalar Django y a iniciar el proyecto.

  Inicializo una app a la cual le asigno el nombre de uploadForm, conecto esta app con el proyecto y proceso a configurar los modelos deacuerdo al modelo relacional.

  ![Descripción de la imagen](/media/models.png)

  Luego creo una carpeta templates, donde ubico las 2 vistas de frontend sin poner estilos css. Creo una carpeta layout con un archivo base.html.

  Luego configuro las rutas propias para la aplicacion uploadForm en el archivo urls.py, utilizo params para compartir informacion entre los dos vistas.

  En el archivo views.py he definido 2 metodos, cada metodo es ejecutado por una vista. Para este caso un metodo es llamado uploadFile() y otro fileResult().

  uploadFile(): este metodo se encarga de toda la logica de la vista upload/, donde se realiza la carga, apertura, procesamiento de datos, validacion y persistencia de los datos.

  fileResult(): Este metodo se encarga de la logica de la vista fileresult/<nombre_archivo> , consulta base de datos y transfiere esta informacion al html para luego se procesado.

  Para terminar verifico los requerimientos y hago pruebas para ver que si se cumplen, al ver que la funcionalidad es correcta, proceso a dar estilos css a la aplicacion. 

  Para dar estilos hago uso de Bootstrap, incluyo Bootstrap's CSS y JS en el archivo base.html ubicado en /templates/layout/base.html. Esto me permite que las vistas que heredan de base.html puedan usar bootstrap.

  Por ultimo aplico a cada vista los estilos que me parecen mas convenientes para cumplir con los Mockups.

  * * *
- Manual de instalación: Con los pasos detallados para poder ejecutar su solución:

    1. instalar python [desde aqui](https://www.python.org/) y añadirlo al path para poder usar el comando python desde consola.
    2. instalar virtualenv <pre><code>pip install virtualenv</code></pre>
    3. Clonar este repositorio y entrar en la carpeta.
    4. Crear un entorno virtual para posteriormente instalar las librerias del proyecto:<pre><code>virtualenv venv</code></pre>
    5. Activar el entorno virtual de nuestro proyecto:<pre><code>.\venv\Scripts\activate</code></pre>
    6. instalar todas las librerias y frameworks:
        - Django
        - mysqlclient
        - PyMySQL
        <pre><code>pip install django mysqlclient pymysql</code></pre> 
    7. en el directorio gemasas localizar el archivo settings.py y configurar USER y PASSWORD en DATABASES.<pre><code>DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': 'localhost',
        'PORT': '3306',
        'USER': 'root',
        'PASSWORD': '12345',
        'NAME': 'gemasas',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
        }
    }
}</code></pre>
    8. Luego desde mysql vamos a ejecutar el siguiente comando para crear la base de datos gemasas: <pre><code>create database gemasas;</code></pre>
    9. Luego desde la carpeta raiz del proyecto ejecutar el comando: <pre><code>python manage.py migrate</code></pre>
    10. Luego ejecutar desde mysql en el orden en que se presentan:
        1.  <pre><code>INSERT INTO uploadForm_estado (name) VALUES ('activo'); </code></pre>
        2.  <pre><code>INSERT INTO uploadForm_estado (name) VALUES ('inactivo');</code></pre>
        3.  <pre><code>INSERT INTO uploadForm_estado (name) VALUES ('espera');</code></pre>
    11.por ultimo se puede ejecutar el proyecto con el siguiente comando desde la carpeta raiz del proyecto:<pre><code>python manage.py runserver</code></pre>
    12.Para ver la aplicacion dirigete a la ruta upload:<pre><code>http://127.0.0.1:8000/upload/</code></pre><pre><code>localhost:8000/upload/</code></pre> 


  * * *
- Tiempo real de solución


    5 horas y 45 minutos.
