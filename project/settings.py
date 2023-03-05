import os
from environs import Env

env = Env()
env.read_env()
os.environ.setdefault('DEBUG', 'True')
os.environ.setdefault('ALLOWED_HOSTS', '[*]')
os.environ.setdefault('SECRET_KEY', 'SECRET_KEY')
db_engine = env('ENGINE')
db_host = env('HOST')
db_port = env('PORT')
db_name = env('NAME')
db_user = env('USER')
db_password = env('PASSWORD')
SECRET_KEY = env('SECRET_KEY')
allowed_hosts = env('ALLOWED_HOSTS')
DEBUG = env.bool('DEBUG')

DATABASES = {
    'default': {
        'ENGINE': db_engine,
        'HOST': db_host,
        'PORT': db_port,
        'NAME': db_name,
        'USER': db_user,
        'PASSWORD': db_password,
    }
}

INSTALLED_APPS = ['datacenter']

ROOT_URLCONF = 'project.urls'

ALLOWED_HOSTS = allowed_hosts


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
    },
]

DEBUG = DEBUG

USE_L10N = True

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
