import os
# este archivo lo vamos a importar desde Settings después

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) #Esto me permite obtener la ruta del directorio de mi proyecto

SQLITE = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR,'db/sqlite/de.sqlite3'),
    }
}

POSTGRESQL = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'db',
        'USER': 'postgres',
        'PASSWORD':'tooR',
        'HOST': 'localhost',
        'PORT': '5433'
    }
}