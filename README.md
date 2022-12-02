## Prueba JERRE JERRE

- Tiempo planeado de solución


  Para completar el nuevo requerimiento el tiempo planeado para dar solucion es de 45 minutos.

  * * *
- Explicación de su solución
  
  En este caso como es un nuevo requerimiento sobre el modelo de datos, primero que todo hago la modificacion al modelo relacional, para luego implemetarlo en el proyecto con Django, de la siguiente manera:


  Modelo relacional modificado:
  ![Descripción de la imagen](/media/relationalmodel.png)


  Modelos de la app de Django modificados:
  ![Descripción de la imagen](/media/modelDjango.png)

  Se modifica tambien el codigo para insertar usuarios, agregando el revisor.

  Modelos de la app de Django modificados:


  ![Descripción de la imagen](/media/add_user_model.png)
  
  y para finalizar se agrea un nuevo valor a la tabla en Django Ninja para que este cree el HTML dinamico deacuerdo a los datos consultados en la base de datos.

  ![Descripción de la imagen](/media/Django_Ninja_UA.png)
  
  * * *
- Manual de instalación: Con los pasos detallados para poder ejecutar su solución:

    1. instalar python [desde aqui](https://www.python.org/) y añadirlo al path para poder usar el comando python desde consola.
    2. instalar virtualenv <pre><code>python install virtualenv</code></pre>
    3. Clonar este repositorio y entrar en la carpeta.
    4. Crear un entorno virtual para posteriormente instalar las librerias del proyecto:<pre><code>python virtualenv venv</code></pre>
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
    1. Luego desde mysql vamos a ejecutar el siguiente comando para crear la base de datos gemasas: <pre><code>create database gemasas;</code></pre>
    2. Luego desde la carpeta raiz del proyecto ejecutar el comando: <pre><code>python manage.py migrate</code></pre>
    3.  Luego ejecutar desde mysql en el orden en que se presentan:
        1.  <pre><code>USE gemasas;<br>INSERT INTO uploadForm_revisor (`name`, `surname`) VALUES ('name', 'Revisor1'); <br> INSERT INTO uploadForm_revisor (`name`, `surname`) VALUES ('name', 'Revisor2'); <br> INSERT INTO uploadForm_revisor (`name`, `surname`) VALUES ('name', 'Revisor3'); <br> INSERT INTO uploadForm_revisor (`name`, `surname`) VALUES ('name', 'Revisor4'); <br> INSERT INTO uploadForm_revisor (`name`, `surname`) VALUES ('name', 'Revisor5'); <br> INSERT INTO uploadForm_revisor (`name`, `surname`) VALUES ('name', 'Revisor6'); <br> INSERT INTO uploadForm_revisor (`name`, `surname`) VALUES ('name', 'Revisor7'); <br> INSERT INTO uploadForm_revisor (`name`, `surname`) VALUES ('name', 'Revisor8'); <br> INSERT INTO uploadForm_estado (name) VALUES ('activo'); <br> INSERT INTO uploadForm_estado (name) VALUES ('inactivo'); <br> INSERT INTO uploadForm_estado (name) VALUES ('espera');</code></pre>
    11.por ultimo se puede ejecutar el proyecto con el siguiente comando desde la carpeta raiz del proyecto:<pre><code>python manage.py runserver</code></pre>



  * * *
- Tiempo real de solución


    1 hora y 7 minutos.