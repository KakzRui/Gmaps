# Gmaps
What the project is?
When we run this application, it shows google map and below user can see the Addresses which are available in DB.
When user clicks on the address, the pointer will be pin pointed in the google maps with exact locality of the address.
User can change the address by dragging the pin point to his desired location and can save the new geo coordinates to the DB.

Below are the softwares to be installed to run this project

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
