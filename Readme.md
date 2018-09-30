

##  **Django Framework Installation and Basic Commands**



**Download  django**</br>
git clone https://github.com/django/django.git

**Install django**</br>
pip install -e django

**Create new django project**</br>
jango-admin startproject *projectName*

**To run django server**</br>
python manage.py runserver

**Create new app**</br>
python manage.py startapp *applicationName*

**Sync with the database, app etc. which define in settings.py**</br>
python manage.py migrate

**Update the database**</br>
python manage.py makemigration *applicationName*
python manage.py migrate

**Check Sql query**</br>
python manage.py sqlmigrate *applicationName* 001
