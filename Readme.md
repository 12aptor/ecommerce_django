# ecommerce_django


## Comandos para crear el proyecto
    
    - python -m venv venv                            (crea mi entorno virtual)
    - source venv/Scripts/activate                   (activa mi entorno virtual)
    - pip install django djangorestframework         (instala las librerias que necesito para crear mi proyecto)
    - django-admin startproject ecommerce_django     (crea el proyecto del proyecto)
    - django-admin startapp almacen                  (crea una nueva aplicación)

    ``` Creamos models, serializers, views y urls ```
    - python manage.py makemigrations                 (crea las migraciones)
    - python manage.py migrate                        (ejecuta las migraciones)

    ``` Documentar mi proyecto```
    [https://github.com/axnsan12/drf-yasg/](https://github.com/axnsan12/drf-yasg/)
    - pip install -U drf-yasg