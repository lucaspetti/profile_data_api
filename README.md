# Profile Data API

A simple Django app using the Rest Framework to retrieve data for my online profile.

### Setup

Python version: 3.6.9

Django version: 3.0.6

### Running the app

Make sure you have python and Django installed on your machine, then run the migrations:

`python manage.py makemigrations`

`python manage.py migrate`

To serve the app:

`python manage.py runserver`

You may want to create a super user, or admin user. To do that just run:

`python manage.py createsuperuser`

And enter the desired username and password.

#### Fixtures

There is a standard file with fixtures for skills records. You can edit the data there and populate the database with:

`python manage.py loaddata skills.json`

Similar JSON files can be created for the other models.
