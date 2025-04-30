import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = b'\xb9k\xdf@\x0e\x1f(\xf2\xb0\xd0\xcb?Y\xdcN\x19G\x12e\xa8\x8b\xe5\xccS'

DEBUG = True

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.staticfiles',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.auth',
    'django.contrib.messages',
    'app',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',           # <<< Added for basic security
    'django.contrib.sessions.middleware.SessionMiddleware',    # <<< Added for session management
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',               # <<< Added for form protection
    'django.contrib.auth.middleware.AuthenticationMiddleware', # <<< Added for auth/session linking
    'django.contrib.messages.middleware.MessageMiddleware',    # <<< Optional, but recommended
    'django.middleware.clickjacking.XFrameOptionsMiddleware',  # <<< Optional, for security
]

ROOT_URLCONF = 'app.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'app', 'templates')],
        'APP_DIRS': True,
    },
]

WSGI_APPLICATION = 'app.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db', 'skyvault.db'),
    }
}

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'app', 'static'),
]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

SESSION_ENGINE = 'django.contrib.sessions.backends.db'