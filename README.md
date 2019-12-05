# Amino Acids

Amino Acids is a Django web app that simulates a simple online student enlistment system

## Getting Started

Before running the server, the following python packages must first be installed:

Django and django-admin:

```
$ pip install django
$ pip install django-admin
```

Django widget tweaks: for rendering form fields in templates:

```
$ pip install django-widget-tweaks
```

## Running the server

To start the server, type the following command while in the 'studentenlistment' 
directory (root django project folder):

```
$ python manage.py runserver 8000
```

### Initial setup

This current project may already have an administrator and a few user records 
in the db. The default admin credentials are as follows:

```
username: admin
password: admin
```

However, if you want to start with a new, clean database, use the following 
command:

```
$ python manage.py flush
```

After clearing the db, a new administrator (superuser) must first be created to 
ensure proper adminstrator functions in the future.
This admin may be deleted when other admins are present. Type in the 
following command:

```
$ python manage.py createsuperuser
```

Provide your own credentials for your first admin.

### Adding new classes

Colleges, along with their respective degree programs can be created in the 
admin site. Click the 'Colleges' link from the 'Main' section to display the 
list of available classes and to add a new college or course

Before you add a class, the course must first be defined. Select the 'Courses'
link from the 'Main' section to create your courses. The courses you add will
be part of the course selection in your class.
