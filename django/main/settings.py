import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = os.getenv('SECRET_KEY')
DEBUG = os.getenv('DEBUG') in [True, 'True', 'true']
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '').split(',')
ENVIRONMENT = os.getenv('ENVIRONMENT')

TESTING = 'test' in sys.argv

ADMINS = [
    ('Ryan Allen', 'allenryan14@gmail.com'),
    ('Kevan Swanberg', 'kevswanberg@gmail.com'),
    ('Jeremy Drager', 'jdrager22@gmail.com'),
]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'storages',

    'games',
    'personnel',
    'seasons',
    'venues',
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

ROOT_URLCONF = 'main.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'main/templates/'),
        ],
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

WSGI_APPLICATION = 'main.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': os.getenv('POSTGRES_HOST'),
        'PORT': os.getenv('POSTGRES_PORT'),
        'NAME': os.getenv('POSTGRES_DB'),
        'USER': os.getenv('POSTGRES_USER'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD'),
    }
}

AUTH_USER_MODEL = 'personnel.User'
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]

# LOGIN_REDIRECT_URL = '/'
# LOGOUT_REDIRECT_URL = LOGIN_REDIRECT_URL
# LOGIN_URL = '/login'

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATICFILES_DIRS = (os.path.join(BASE_DIR, 'main/static/'),)

STATIC_DIRNAME = 'static'
STATIC_URL = f'/{STATIC_DIRNAME}/'
STATIC_ROOT = os.path.join(BASE_DIR, f'.{STATIC_DIRNAME}')

MEDIA_DIRNAME = 'media'
MEDIA_URL = f'/{MEDIA_DIRNAME}/'
MEDIA_ROOT = os.path.join(BASE_DIR, f'.{MEDIA_DIRNAME}')

AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = os.getenv('AWS_STORAGE_BUCKET_NAME')
if AWS_STORAGE_BUCKET_NAME:
    AWS_DEFAULT_ACL = None
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATIC_DIRNAME}/'
    STATICFILES_STORAGE = 'main.storages.StaticStorage'

    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIA_DIRNAME}/'
    DEFAULT_FILE_STORAGE = 'main.storages.MediaStorage'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend' if DEBUG else \
                'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.getenv('EMAIL_HOST')
EMAIL_PORT = os.getenv('EMAIL_PORT')
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS = os.getenv('EMAIL_USE_TLS') in [True, 'True', 'true']
DEFAULT_FROM_EMAIL = f'noreply@{EMAIL_HOST}'
SERVER_EMAIL = DEFAULT_FROM_EMAIL
