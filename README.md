# highway-maps

Sample application for searching highways and drawing them on google maps.

## Technologies

I basically wanted an excuse to try out:

* Django
* Backbone.js
* RequireJS

## Configuration

You need to configure a couple of paths on `settings.py`:

* *DATABASES.default.NAME*: Where the sqlite3 DB will be created.
* *MEDIA_ROOT*: Full path to the *media* directory on the project's root directory.
* *TEMPLATE_DIRS*: Full path to the *templates* directory on the project's root directory.

## Setup

* Install Django (I used version 1.2.3).
* Create the database tables with `python manage.py syncdb` (create an admin user when prompted).
* Load some data into the database `python manage.py loaddata db/prod.json`.
* Start the development server `python manage.py runserver`.

## URLs

* Django's admin (CRUD operations on the models): [http://localhost:8000/admin](http://localhost:8000/admin)
* Sample application built with backbone.js: [http://localhost:8000/carreteras](http://localhost:8000/carreteras)

You might want to try some states with data like:

* Tamaulipas.
* Guerrero.
* Hidalgo.
* Mexico.
* Morelos.
* Nuevo León.
* San Luis Potosí.

