"""
ASGI config for config project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os
from channels.routing import ProtocolTypeRouter
from strawberry_django.routers import AuthGraphQLProtocolTypeRouter
from django.core.asgi import get_asgi_application
from book.schema import schema

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django_asgi_app = get_asgi_application()


application = AuthGraphQLProtocolTypeRouter(
    schema,
    django_application=django_asgi_app,
)