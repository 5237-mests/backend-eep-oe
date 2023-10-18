"""
Django settings for online_exam project.

Generated by 'django-admin startproject' using Django 4.1.7.
"""
from pathlib import Path
from os import getenv
from dotenv import load_dotenv
load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = getenv("DJANGO_SECRET_KEY", '''django-insecure-c--w0i@@hm!sd2wzta!
!_aavihk=@mnq(oo9ojzs(0+sq-cs+0''')

DEBUG = True
ALLOWED_HOSTS = []
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'users',
    'questions',
    'rest_framework',
    'corsheaders',
    "home",
]
AUTH_USER_MODEL = "users.Employee"
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    "corsheaders.middleware.CorsMiddleware",  # allow CORS
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
ROOT_URLCONF = 'online_exam.urls'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],
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

WSGI_APPLICATION = 'online_exam.wsgi.application'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': getenv("MYSQL_DB"),
        'USER': getenv("MYSQL_USER"),
        "PASSWORD": getenv("MYSQL_PASSWORD"),
        "HOST": getenv("MYSQL_HOST"),
        "PORT": getenv("MYSQL_PORT"),
    }
}
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME':
        '''django.contrib.auth.password_validation.UserAttributeSimilarityValidator''',
    },
    {
        'NAME':
        '''django.contrib.auth.password_validation.MinimumLengthValidator''',
    },
    {
        'NAME':
        '''django.contrib.auth.password_validation.CommonPasswordValidator''',
    },
    {
        'NAME':
        '''django.contrib.auth.password_validation.NumericPasswordValidator''',
    },
]
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Addis_Ababa'

USE_I18N = True

USE_TZ = True
STATIC_URL = 'static/'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
    ],
    "DEFAULT_PERMISSION_CLASSES": [
                                "rest_framework.permissions.AllowAny"
    ]
}
CORS_ALLOWED_ORIGINS = [
                        getenv("ALLOWED_H"),
                        getenv("ALLOWED_HH")]
CORS_ORIGIN_ALLOW_ALL = False
CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_WHITELIST = [
                         getenv("ALLOWED_H"),
                         getenv("ALLOWED_HH")]

CSRF_TRUSTED_ORIGINS = [
                        getenv("ALLOWED_H"),
                        getenv("ALLOWED_HH")]
CSRF_COOKIE_HTTPONLY = False
CSRF_COOKIE_SAMESITE = "Lax"
SESSION_COOKIE_SAMESITE = "Lax"
CSRF_COOKIE_SECURE = False
CSRF_HEADER_NAME = "HTTP_X_CSRFTOKEN"
CSRF_COOKIE_NAME = "csrftoken"
SESSION_COOKIE_NAME = "sessionid"
CORS_ALLOW_HEADERS = [
    "csrftoken",
    'content-type',
    'x-csrftoken',
    'sessionid',
    'authorization'
]
CORS_EXPOSE_HEADERS = ["Content-Type", "X-CSRFToken", "Cookie"]
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = getenv('EMAIL_HOST')
EMAIL_PORT = getenv('EMAIL_PORT')
EMAIL_HOST_USER = getenv("MAIL_USER")
EMAIL_HOST_PASSWORD = getenv("MAIL_PASSWORD")
EMAIL_USE_TLS = True
