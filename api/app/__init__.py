import os
import logging.config
from flask import Flask
from app.views.signup import signup

__all__ = ["app"]

app = Flask(__name__)
app.register_blueprint(signup)

app.config.from_object("app.settings.default")
if os.environ.get("APP_SETTINGS"):
    app.config.from_envvar("APP_SETTINGS")

FLASK_ENV = os.environ.get("FLASK_ENV")

def require_debug_true_filter():
    def filter(record):
        return FLASK_ENV
    return filter

def require_debug_false_filter():
    def filter(record):
        return not FLASK_ENV
    return filter

LOGGING_CONFIG_DICT = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "long": {
            "format": "[APP] {levelname} {asctime} {module} "
                      "{name}.{funcName}:{lineno:d}: {message}",
            "style": "{"
        },
        "short": {
            "format": "[APP] {levelname} [{asctime}] {message}",
            "style": "{"
        }
    },
    "filters": {
        "debug_true": {
            "()": require_debug_true_filter
        },
        "debug_false": {
            "()": require_debug_false_filter
        }
    },
    "handlers": {
        "console": {
            "level": "INFO",
            "class": "logging.StreamHandler",
            "formatter": "short",
            "filters": ["debug_false"]
        },
        "console_debug": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "long",
            "filters": ["debug_true"]
        }
    },
    "loggers": {
        "app": {
            "handlers": ["console", "console_debug"],
            "level": "DEBUG"
        }
    }
}


logging.config.dictConfig(LOGGING_CONFIG_DICT)
