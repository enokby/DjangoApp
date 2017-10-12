# Django CRUD Example Apps

This is a small Django project that adds and view email entries

## Install Required Packages

The Django CRUD project only need a single Python package "Django", it was built and
tested with Django 1.8.x version. To install it use the following command:

    pip install -r requirements.txt


## Running the Application

Before running the application we need to create the needed DB tables:

    ./manage.py migrate

Now you can run the development web server:

    ./manage.py runserver 80

To access the applications go to the URL <http://localhost/>

