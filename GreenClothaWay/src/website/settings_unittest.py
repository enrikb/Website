from website.settings_default import *

# SECURITY WARNING: keep the secret key used in production secret!
# see django doc for generating secrete key and do it
SECRET_KEY = ''

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['www.greenclothaway.eu', 'greenclothaway.eu', 'localhost', '78.46.122.92', '2a01:4f8:c2c:3a34::1', '127.0.0.1']

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases
# enter db specs fitting your local machine

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'testbase',
    }
}
