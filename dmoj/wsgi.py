import os

from django.core.wsgi import get_wsgi_application  # noqa: E402, django must be imported here

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dmoj.settings')

try:
    import MySQLdb  # noqa: F401, imported for side effect
except ImportError:
    import pymysql

    pymysql.install_as_MySQLdb()
application = get_wsgi_application()
