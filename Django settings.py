import os

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get('DB_NAME', 'notesdb'),
        'USER': os.environ.get('DB_USER', 'notesuser'),
        'PASSWORD': os.environ.get('DB_PASSWORD', 'notespass'),
        'HOST': os.environ.get('DB_HOST', 'localhost'),
        'PORT': '3306',
    }
}
