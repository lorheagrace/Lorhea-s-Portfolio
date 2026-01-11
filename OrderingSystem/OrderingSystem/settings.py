"""
Django settings for OrderingSystem project.
"""

import os
from pathlib import Path

# ======================
# BASE DIRECTORY
# ======================
BASE_DIR = Path(__file__).resolve().parent.parent

# ======================
# SECURITY
# ======================
SECRET_KEY = 'django-insecure-_6q2_!)q7_d$j-)^z^w_5(5ok^a(w*+$h-s=#$^ce)0kuv1s7-'

DEBUG = False  # MUST be False in production

ALLOWED_HOSTS = ["*"]

# ======================
# APPLICATIONS
# ======================
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'MSMEOrderingWebApp',
]

# ======================
# MIDDLEWARE
# ======================
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',

    # WhiteNoise for static files
    'whitenoise.middleware.WhiteNoiseMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ======================
# URLS & WSGI
# ======================
ROOT_URLCONF = 'OrderingSystem.urls'
WSGI_APPLICATION = 'OrderingSystem.wsgi.application'

# ======================
# TEMPLATES
# ======================
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

# ======================
# DATABASE
# ======================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# ======================
# PASSWORD VALIDATION
# ======================
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ======================
# INTERNATIONALIZATION
# ======================
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# ======================
# STATIC FILES (VERY IMPORTANT)
# ======================
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'  # where collectstatic will gather files

STATICFILES_DIRS = [
    BASE_DIR / 'MSMEOrderingWebApp' / 'static',  # include your app's static folder
]

# Optional: use WhiteNoise for production
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"


# ======================
# MEDIA FILES
# ======================
MEDIA_URL = '/Media/'
MEDIA_ROOT = BASE_DIR / 'Media'

# ======================
# DEFAULT PK
# ======================
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
