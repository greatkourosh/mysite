from mysite.settings import *
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# from django import middleware


SECRET_KEY = "django-insecure-*45z$-bd4n)weg6e6*i^2gn)2f66gqc_fxr_5&#^d=z9**cp@*"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', '192.168.1.0/24',]

# INSTALLED_APPS = []

if DEBUG:
    MIDDLEWARE += [
        "django.middleware.clickjacking.XFrameOptionsMiddleware",
    ]
    

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

STATIC_ROOT = BASE_DIR / "static"
MEDIA_ROOT = BASE_DIR / "media"

STATICFILES_DIRS = [
    BASE_DIR / "statics",
    # "/var/www/static/",
]
    
# sites framework
SITE_ID = 2

X_FRAME_OPTIONS = "SAMEORIGIN"