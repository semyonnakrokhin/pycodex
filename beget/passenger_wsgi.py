import os, sys
sys.path.insert(0, '/home/a/amirkhln/amirkhln.beget.tech/pycodex_django')
sys.path.insert(1, '/home/a/amirkhln/amirkhln.beget.tech/venv_pycodex/lib/python3.10/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'pycodex.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
