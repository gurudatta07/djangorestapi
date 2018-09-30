

##  **Django Framework Installation and Basic Commands**



**Download  django**
git clone https://github.com/django/django.git

**Install django**
pip install -e django

**Create new django project**
jango-admin startproject *projectName*

**To run django server**
python manage.py runserver

**Create new app**
python manage.py startapp *applicationName*

**Sync with the database, app etc. which define in settings.py**
python manage.py migrate

**Update the database**
python manage.py makemigration *applicationName*
python manage.py migrate

**Check Sql query**
python manage.py sqlmigrate *applicationName* 001
