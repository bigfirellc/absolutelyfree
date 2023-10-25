"""settings.py
"""
import os
import environ

env = environ.Env()
environ.Env.read_env()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = env("SECRET_KEY")

DEBUG = env("DEBUG")

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'absolutelyfree.net', 'www.absolutelyfree.net']

INSTALLED_APPS = [
    'rand.apps.BandConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'import_export',
    'storages',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'absolutelyfree.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'absolutelyfree.wsgi.application'

USE_POSTGRES = os.getenv('USE_POSTGRES') == 'TRUE'

if USE_POSTGRES:
    DATABASES = {
        'default': {
            'ENGINE': env("DATABASE_ENGINE"),
            'NAME': env("DATABASE_NAME"),
            'USER': env("DATABASE_USER"),
            'PASSWORD': env("DATABASE_PASSWORD"),
            'HOST': env("DATABASE_HOST"),
            'PORT': env("DATABASE_PORT"),
        }
    }
else:
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'absolutelyfree', 
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'America/New_York'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Storage stuff

USE_S3 = os.getenv('USE_S3') == 'TRUE'

if USE_S3:
    # Auth to B2 Bucket
    AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
    AWS_STORAGE_BUCKET_NAME = os.getenv('AWS_STORAGE_BUCKET_NAME')
    AWS_S3_REGION_NAME = os.getenv('AWS_S3_REGION_NAME')
    AWS_S3_ENDPOINT_URL = 'https://s3.us-west-000.backblazeb2.com'
    # Settings for Static Files
    STATIC_LOCATION = 'static'
    STATIC_URL = f'{AWS_S3_ENDPOINT_URL}/{AWS_STORAGE_BUCKET_NAME}/{STATIC_LOCATION}/'
    STATICFILES_STORAGE = 'absolutelyfree.storage_backends.StaticStorage'
    # Settings for Media Files
    PUBLIC_MEDIA_LOCATION = 'media'
    MEDIA_URL = f'{AWS_S3_ENDPOINT_URL}/{AWS_STORAGE_BUCKET_NAME}/{PUBLIC_MEDIA_LOCATION}/'
    DEFAULT_FILE_STORAGE = 'absolutelyfree.storage_backends.PublicMediaStorage'
else:
    STATIC_URL = '/staticfiles/'
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    MEDIA_URL = "/mediafiles/"
    MEDIA_ROOT = os.path.join(BASE_DIR, "mediafiles")

STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

CSRF_TRUSTED_ORIGINS = [
    'https://www.absolutelyfree.net',
    'https://s3.us-west-000.backblazeb2.com',
    'https://cdn.jsdelivr.net'
]
