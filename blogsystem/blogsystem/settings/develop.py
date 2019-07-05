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
    # 'debug_toolbar',
    # 'pympler',
    # 'debug_toolbar_line_profiler', 安装失败
    'silk'
]

MIDDLEWARE += [
    # 'debug_toolbar.middleware.DebugToolbarMiddleware',
    'silk.middleware.SilkyMiddleware'
]

INTERNAL_IPS = ['127.0.0.1']


# DEBUG_TOOLBAR_CONFIG = {
#     'JQUERY_URL': ' https://cdn.bootcss.com/jquery/3.3.1/jquery.min.js',
# }

# DEBUG_TOOLBAR_PANELS = [
    # djdt_flamegraph火焰图，由于信号的系统不兼容，windows下无法正常使用，暂时关闭
    #     'djdt_flamegraph.FlamegraphPanel',
    # 'pympler.panels.MemoryPanel',  # 运行报错
    # 'debug_toolbar_line_profiler.panel.ProfilingPanel',
# ]
