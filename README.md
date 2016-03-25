# Gmaps
Install Python 2.7

$ pip install Django==1.9.4
$ brew install postgresql
$ brew install postgis
$ brew install gdal
$ brew install libgeoip

Install Mysql 5.6

Add Below lines of code in settings.py file

TEMPLATES = [
  {
    'DIRS': ['/Users/manoj/Documents/gmaps/templates/'],
  }
]


DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.mysql',
        'ENGINE': 'django.contrib.gis.db.backends.mysql',
        'NAME': 'gmaps',
        'USER': 'root',
        'PASSWORD': 'mysql',
        'OPTIONS': {
          'autocommit': True,
        },
    }
}


To add the tables in DB, run db sync in terminal, below is the command for syncdb

python manage.py makemigrations
python manage.py migrate
