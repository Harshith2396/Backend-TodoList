"""
Django settings for backendToDoList project.

Generated by 'django-admin startproject' using Django 2.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""
from datetime import timedelta
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'e_6^l=-w3c!u5cpskvalmrg9t28g$n6us@tayzlq=j%8k(ph2r'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework','corsheaders','todoList','accounts',
    'rest_framework_simplejwt.token_blacklist',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'backendToDoList.urls'

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

WSGI_APPLICATION = 'backendToDoList.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True  #ALWAYS LEAVE 'True' TO AVOID TIME CONVERTION ERRORS


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
CORS_ORIGIN_ALLOW_ALL=True
AUTH_USER_MODEL='accounts.UserAccounts'
REST_FRAMEWORK = {
"DEFAULT_AUTHENTICATION_CLASSES":[
    'rest_framework_simplejwt.authentication.JWTAuthentication',
    
    
],
#'DEFAULT_PERMISSION_CLASSES': [
 #      'rest_framework.permissions.IsAuthenticatedOrReadOnly',
   #]     DO NOT SPECIFY THIS OPTION AS IT WILL  SET PERMISSION FOR ALL THE VIEW CLASSESS AND AUTHENTICATION WILL BE COMPULSARY ON ALL CLASSESS
}
SIMPLE_JWT={
    'USER_ID_FIELD':'email',
    'ACCESS_TOKEN_LIFETIME':timedelta(minutes=60),
    'SLIDING_TOKEN_LIFETIME': timedelta(minutes=5),
    'AUTH_TOKEN_CLASSES':('rest_framework_simplejwt.tokens.SlidingToken','rest_framework_simplejwt.tokens.AccessToken')
}
CORS_ALLOW_HEADERS =[
    #this is an important  setting which resolves all cors errors  
    #this will be added by a preflight process in the front end such as react or angular
    #this is a custom header added to the http req header 
    'authorization',
    'content-type',
]
CORS_ALLOW_METHODS=[
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    
]
EMAIL_BACKEND ='django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'yourgmailAccount@gmail.com'
EMAIL_HOST_PASSWORD = 'Your Account Password'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_USE_SSL=False