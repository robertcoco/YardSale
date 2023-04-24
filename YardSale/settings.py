"""
Django settings for YardSale project.

Generated by 'django-admin startproject' using Django 4.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-*7ok#@f-ss5kdhh+guwilx9x21p1yh^^3&9sded=$qm#v8+zn4'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

if not DEBUG:
    CSRF_TRUSTED_ORIGINS = ['https://web-production-1350.up.railway.app']

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'shop.apps.ShopConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'crispy_forms',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
]

SITE_ID = 1

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        },
        'OAUTH_PKCE_ENABLED': True,
    }
}
SECURE_SSL_REDIRECT = False
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Agregar aquí
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'shop.middleware.LoginRequiredMiddleware'
]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

ROOT_URLCONF = 'YardSale.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR/ 'templates'],
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

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)


WSGI_APPLICATION = 'YardSale.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}



# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/
import os
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR/'staticfiles'
STATICFILES_DIRS = [
    BASE_DIR/'staticfiles'
]
# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

# settings.py

# Configuración del correo electrónico para enviar correos electrónicos de recuperación de contraseña
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'robertoangelabaddelossantos9@gmail.com'
EMAIL_HOST_PASSWORD = 'knemncxtlbrwzrqc'
DEFAULT_FROM_EMAIL = 'robertoangelabaddelossantos9@gmail.com'


from django.contrib.messages import constants as messages

MESSAGE_TAGS = {
        messages.DEBUG: 'alert-secondary',
        messages.INFO: 'alert-info',
        messages.SUCCESS: 'alert-success',
        messages.WARNING: 'alert-warning',
        messages.ERROR: 'alert-danger',
}

# settings.py
LOGIN_URL = '/shop/'
LOGIN_REDIRECT_URL = '/shop/' # 'home' es la url de la página a la que se redirigirá después de iniciar sesión exitosamente
LOGOUT_REDIRECT_URL = '/accounts/login'
SOCIAL_AUTH_FACEBOOK_KEY = '1020885318881585'  # App ID
SOCIAL_AUTH_FACEBOOK_SECRET = 'd1c41757543f8bea48deecfbbc383562'  # App Secret
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '832957171751-v3htrqpna63n7hikp3q11odem1uvhkhk.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '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'

