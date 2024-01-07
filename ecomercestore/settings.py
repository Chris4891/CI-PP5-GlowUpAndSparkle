"""
Django settings for ecomercestore project.

Generated by 'django-admin startproject' using Django 3.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '-95t%=#4o3@l-(-%ok9*h%n3!0(sdchjn%+_$5#umaj-!3bg*7'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Full',
        'toolbar_Custom': [
            ['Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript'],
            ['NumberedList', 'BulletedList', 'Blockquote', 'HorizontalRule'],
            ['Format', 'Styles', 'RemoveFormat'],
            ['Link', 'Unlink', 'Image', 'Table'],
            ['Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord'],
            ['Undo', 'Redo', 'Find', 'SelectAll', 'Scayt'],
            ['Maximize', 'Source'],
        ],
        'extraPlugins': 'image2,uploadimage',
        'image2_alignClasses': ['image-align-left', 'image-align-center', 'image-align-right'],
        'removeDialogTabs': 'image:advanced;link:advanced',
    }
}
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'store',
    'ckeditor',
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

ROOT_URLCONF = 'ecomercestore.urls'

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

WSGI_APPLICATION = 'ecomercestore.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = "/images/"
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
MEDIA_ROOT = BASE_DIR

# settings.py

STRIPE_PUBLIC_KEY = 'pk_test_51ORcH4L6KLdg6T2ndLB0iextSvsGZfIESd1eagjIkpram3tewxvR67pJU7BFbCWZu6R9Nd5QVEGmmuSdjerenjNL00OEamGWkn'
STRIPE_SECRET_KEY = 'sk_test_51ORcH4L6KLdg6T2nqmRzBBb2Pva57ZeG96ImKgzSYsRHsrcCtlWhLDbdlomA5EEzJVGsU8JgX2dXXEoHiWymUJtR008JVQ9KV0'


# settings.py
# settings.py

# Email configuration
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587  # For TLS
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False  # Set to False for TLS
EMAIL_HOST_USER = 'glowupsparkle@gmail.com'  # Your Gmail email address
EMAIL_HOST_PASSWORD = 'Hokuspokus-1984!!'  # Your Gmail password or app-specific password
