import logging

from os import getenv
from logging.config import dictConfig

# default for dev environment
_APP_LOG_LEVEL = getenv('APP_LOG_LEVEL', 'DEBUG')

dictConfig({
    'version': 1,
    'disable_existing_loggers': True,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': _APP_LOG_LEVEL,
    },
})

logging = logging
