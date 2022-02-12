# My Blog

## Table of contents
* [Description](#description)
* [Technologies](#requirements)
* [Work](#installation--configuration)
* [Results](#results)

## Description

That's my own blog. Here I'll be able to share with you my opinion about something, a strange point of view, useful facts and interesting moments. 
The project was completely built using Django technologies, PostgreSQL database and AWS S3 statistical data storage space.  
The blog had been deploying at https://my-blog-9zxe3.ondigitalocean.app

## Requirements

Project are using next technologies:
* Django 4.0.1
* django-ckeditor 6.2.0
* Pillow 9.0.0
* psycopg2 2.9.3
* dj-database-url 0.5.0
* boto3 1.20.45
* django-storages 1.12.3

## Installation & Configuration

Before installing process, you have to be sure that Python and Git are installed on your device.
```shell
~$ mkdir temp && cd temp
~$ git clone <repo-name>.git
~$ cd my_blog/
~$ python -m venv djangoenv
```
If you use package manager PIP try:
```shell
~$ source djangoenv/bin/activate
~$ pip install -r requirements.txt
```
Now lets configure a little bit our project: You have to create DB into your local PostgresSQL and configure environment variables. Also you could use sqlite DB ( fast run). For this, please overwrite DATABASE variable in settings.py
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```
Now you must setting other environment variables DEBUG
```shell
~$ export DEBUG=True;DEVELOPMENT_MODE=True
```
For using default Django's staticfiles manager, please comment this line into settings.py
```python
from .cdn.conf import *  # comment this
```
Notice, functions that depend on E-Mail SMTP won't be work. So let's complete our installation.
```shell
~$ python manage.py makemigrations && python manage.py migrate
~$ python manage.py createsuperuser # and follow the instructions//
~$ python manage.py runserver
```