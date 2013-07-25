# coding=utf-8
#
# Copyright (c) 2008-2013 by zenzire - http://www.zenzire.com
# Author Marcin Mierzejewski
#

import os
import sys
from django.conf import global_settings

##############################################################################
# Core variable definition
#

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
EXAMPLE_ROOT =  os.path.abspath(os.path.join(os.path.dirname(__file__)))
sys.path.append(PROJECT_ROOT)

DEBUG = True
TEMPLATE_DEBUG = DEBUG

##############################################################################
# I18N and L10N settings
#
TIME_ZONE = 'Europe/Warsaw'
LANGUAGE_CODE = 'en'
SITE_ID = 1
USE_I18N = True
USE_L10N = False
USE_TZ = False
DATETIME_FORMAT = 'F j, Y'
SECRET_KEY = 'Y6BIhFfzxDQsRGoe0kjEBFepz9D4b9YRbdUKJ1qfYaCmulyqAI1QdWCyyzp2V932gxute2a9DC8QvA5Z'

##############################################################################
# Email 
#
ADMINS = ()
MANAGERS = ADMINS
INTERNAL_IPS = ('127.0.0.1',)

##############################################################################
# Database 
#
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '%s/database.sqlite' % EXAMPLE_ROOT,
        'OPTIONS': { 'timeout': 20, },
    }
}

##############################################################################
# Media and static
#
MEDIA_ROOT = os.path.join(EXAMPLE_ROOT, 'media')
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(EXAMPLE_ROOT, 'static')
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'klisha', 'static'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

##############################################################################
# Templates, middlewares and applications
#
ROOT_URLCONF = 'example.urls'
WSGI_APPLICATION = 'example.wsgi.application'

TEMPLATE_DIRS = ( os.path.join(EXAMPLE_ROOT, 'templates'), )
MIDDLEWARE_CLASSES = global_settings.MIDDLEWARE_CLASSES + ('django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',)
TEMPLATE_CONTEXT_PROCESSORS = global_settings.TEMPLATE_CONTEXT_PROCESSORS + ('klisha.context_processors.settings',)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django_admin_bootstrapped',
    'django.contrib.admin',
    'django.contrib.staticfiles',
    'django.contrib.flatpages',
    'django.contrib.sites',

     # Dependencies
    'south',
    'sorl.thumbnail',
    'compressor',
    'pure_pagination',    
    'klisha',
)

SKIP_SOUTH_TESTS = True
COMPRESS_ENABLED = True
COMPRESS_OUTPUT_DIR = 'cache'

PAGINATION_SETTINGS = {
    'PAGE_RANGE_DISPLAYED': 10,
    'MARGIN_PAGES_DISPLAYED': 2,
}

##############################################################################
# Import local settings
#
try:
    from settings_local import *
    TEMPLATE_DEBUG = DEBUG
except ImportError:
    pass
