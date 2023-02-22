#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main(_env):
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', f'chuthe.settings.{_env}')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":

    env = os.getenv("CHUTHE_ENV", False)
    if env:
        main(env.lower())
    else:
        raise EnvironmentError(f'PLEASE EXPORT YOUR ENV `CHUTHE_ENV: ["PROD", "STAGING", "DEV", "LOCAL"]`')
