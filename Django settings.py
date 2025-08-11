import os

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get('DB_NAME', 'notesdb'),
        'USER': os.environ.get('DB_USER', 'notesuser'),
        'PASSWORD': os.environ.get('DB_PASSWORD', 'notespass'),
        'HOST': os.environ.get('DB_HOST', 'db'),  # use service name from docker-compose
        'PORT': os.environ.get('DB_PORT', '3306'),
    }
}
