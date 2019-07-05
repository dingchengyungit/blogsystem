from .base import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'blogsystem',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': '127.0.0.1',
        'PORT': '3306'
    }
}

INSTALLED_APPS += [
    'debug_toolbar',
]

MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

INTERNAL_IPS = ['127.0.0.1']


# djdt_flamegraph火焰图，由于信号的系统不兼容，windows下无法正常使用，暂时关闭
# DEBUG_TOOLBAR_PANELS = [
#     'djdt_flamegraph.FlamegraphPanel',
# ]