import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


SQLITE = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'dbterratur.sqlite3')
    }
}


"""
MYSQL = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'db_terratur_mysql',
        'USER': 'root',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '3306'
    }
}

"""

