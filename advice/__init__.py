from django.apps import AppConfig
import os

default_app_config = 'advice.AdviceConfig'

VERBOSE_APP_NAME = u"投诉建议"


def get_current_app_name(_file):
    return os.path.split(os.path.dirname(_file))[-1]


class AdviceConfig(AppConfig):
    name = get_current_app_name(__file__)
    verbose_name = VERBOSE_APP_NAME