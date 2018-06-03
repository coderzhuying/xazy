from django.apps import AppConfig
import os

default_app_config = 'join.JoinConfig'

VERBOSE_APP_NAME = u"加入庄勇"


def get_current_app_name(_file):
    return os.path.split(os.path.dirname(_file))[-1]


class JoinConfig(AppConfig):
    name = get_current_app_name(__file__)
    verbose_name = VERBOSE_APP_NAME