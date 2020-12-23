"""
ASGI config for contatoproj project.
template disponível no url abaixo:
https://github.com/django/django/blob/7f19e3713598a37b0809b5434114140170d12e34/django/conf/project_template/project_name/asgi.py-tpl

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/{{ docs_version }}/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'contatoproj.settings')

application = get_asgi_application()
