"""
Django settings for unilabsAPI project.

Generated by 'django-admin startproject' using Django 3.2.6.

"""

from datetime import timedelta
from pathlib import Path
from decouple import config
import dj_database_url
import os
import django_heroku

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

SECRET_KEY = config('SECRET_KEY')


DEBUG = config('DEBUG',"False")=="True"

ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'https://unilabs-api.herokuapp.com/']

AUTH_USER_MODEL = 'custom_user.User'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Custom
    'custom_user',
    'admin_user',
    'department',
    'lab',
    'lab_manager_user',
    'lab_assistant_user',
    'item_category',
    'display_item',
    'student_user',

    # ThrirdParty
    'rest_framework',
    'drf_yasg',
    'dj_database_url',
    'django_extensions',
    'knox'
]

SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS':{
        'Token':{
            'type':'apiKey',
            'name':'Authorization',
            'in':'header',
        }
    }
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'unilabsAPI.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'unilabsAPI.wsgi.application'


# Database for github workflow and other
if(config('GITHUB_WORKFLOW',None)):
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
else:
    DATABASES = {
        'default': dj_database_url.parse(config('DATABASE_URL'),engine='django.db.backends.postgresql',ssl_require=config('SSL_MODE','False')=='True',conn_max_age=None),
    }

# Rest framework settings
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'knox.auth.TokenAuthentication',
    ),

}

# Rest Knox framework settings
REST_KNOX = {
  'TOKEN_TTL': timedelta(days=10),
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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


# Internationalization
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
DISABLE_COLLECTSTATIC=1
STATIC_URL = '/static/'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Email Service Setup
EMAIL_BACKEND = "sendgrid_backend.SendgridBackend"
SENDGRID_API_KEY = config("SENDGRID_API_KEY")
SENDGRID_SANDBOX_MODE_IN_DEBUG=config('SENDGRID_SANDBOX_MODE_IN_DEBUG','True')==True # set to true in debug mode to use sandbox
SENDGRID_ECHO_TO_STDOUT=True # Echo the mail output to console

# Heroku deployment setup
django_heroku.settings(locals(), test_runner=False)
