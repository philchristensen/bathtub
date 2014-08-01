#!/usr/bin/env python

import os, os.path
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bathtub.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
