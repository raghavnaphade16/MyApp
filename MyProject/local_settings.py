import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'MyDb',
        'USER':'postgres',
        'PASSWORD':  'India@8793',
        'HOST':'localhost'
    }
}
