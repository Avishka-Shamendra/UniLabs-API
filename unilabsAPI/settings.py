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
    'item',
    'lecturer_user',
    'request',

    # ThrirdParty
    'rest_framework',
    'drf_yasg',
    'dj_database_url',
    'django_extensions',
    'knox',
    'cloudinary_storage',
    'cloudinary',
    "corsheaders",
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
    "corsheaders.middleware.CorsMiddleware",
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'csp.middleware.CSPMiddleware', # thrirdParty from django-csp
]

SECURE_HSTS_SECONDS = 31536000
SECURE_SSL_REDIRECT = config('DEBUG',"False")=="False" # if debug false set this to true
SECURE_HSTS_INCLUDE_SUBDOMAINS = config('DEBUG',"False")=="False"
SECURE_HSTS_PRELOAD = config('DEBUG',"False")=="False"
SESSION_COOKIE_SECURE = config('DEBUG',"False")=="False"
CSRF_COOKIE_SECURE = config('DEBUG',"False")=="False"

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
  'TOKEN_TTL': timedelta(days=3),
  'AUTO_REFRESH': True, # This defines if the token expiry time is extended by TOKEN_TTL each time the token is used.
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
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

#Cloudinary settings

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': config('CLOUDINARY_NAME'), # add these to heroku and github
    'API_KEY': config('CLOUDINARY_KEY'),
    'API_SECRET': config('CLOUDINARY_SECRET'),
}

if config("ENVIRONMENT", '') == 'PRODUCTION':
    DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
else:
    MEDIA_URL = '/media/'
    MEDIA_ROOT = config('BASE_DIR', 'media')

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Email Service Setup
EMAIL_BACKEND = "sendgrid_backend.SendgridBackend"
SENDGRID_API_KEY = config("SENDGRID_API_KEY")
SENDGRID_SANDBOX_MODE_IN_DEBUG=config('SENDGRID_SANDBOX_MODE_IN_DEBUG','True')==True # set to true in debug mode to use sandbox
SENDGRID_ECHO_TO_STDOUT=True # Echo the mail output to console

CORS_ORIGIN_WHITELIST= ('http://localhost:3000', config('FRONTEND_URL'))

# Heroku deployment setup
django_heroku.settings(locals(), test_runner=False)


# content security policy

# default source as self
# CSP_DEFAULT_SRC = ("'self'", )

# style from our domain only
# CSP_STYLE_SRC = ("'self'","sha256-47DEQpj8HBSa+/TImW+5JCeuQeRkm5NMpJWZG3hSuFU=")

# scripts from our domain and google analytics
# CSP_SCRIPT_SRC = ("'self'","www.google-analytics.com",)


# images from our domain and cloudinary
# CSP_IMG_SRC = ("'self'",
#     config("CLOUDINARY_NAME")+".cloudinary.com",
#     "www.cloudinary.com",
#     "www.google-analytics.com",)
  
# loading manifest, workers, frames, etc
# CSP_FONT_SRC = ("'self'", )
# CSP_CONNECT_SRC = ("'self'", "www.google-analytics.com" )
# CSP_OBJECT_SRC = ("'self'", )
# CSP_BASE_URI = ("'self'", )
# CSP_FRAME_ANCESTORS = ("'self'", )
# CSP_FORM_ACTION = ("'self'", )
# CSP_INCLUDE_NONCE_IN = ('script-src', )
# CSP_MANIFEST_SRC = ("'self'", )
# CSP_WORKER_SRC = ("'self'", )
# CSP_MEDIA_SRC = ("'self'", )