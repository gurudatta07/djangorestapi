Django framework installation and Basic commands

Download from
git clone https://github.com/django/django.git

Install django
pip install -e django

Create new django project
jango-admin startproject <projectName>

Run django server
python manage.py runserver

Create new app
python manage.py startapp <appName>

Sync with the database, app etc. which define in settings.py
python manage.py migrate

Update the db
python manage.py makemigration <appName>
python manage.py migrate

Check Sql query
python manage.py sqlmigrate <appName> 001