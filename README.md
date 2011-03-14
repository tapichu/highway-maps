# highway-maps

Search highways and draw them on google maps.

## Tools

I wanted to play with:

* Django
* Backbone.js
* RequireJS
* Buildout

## Setup

* I recommend crating a _virtualenv_ isolated from your system Python:
    * <code>virtualenv --no-site-packages myenv</code>
    * <code>cd myenv</code>
    * <code>source bin/activate</code> (to activate the sandbox)
    * <code>deactivate</code> (to leave the sandbox)
* Clone this repository: <code>git clone [URL]</code>
* Change directory: <code>cd highway-maps</code>
* Bootstrap _buildout_: <code>python bootstrap.py</code>
* Run buildout: <code>./bin/buildout</code>

## Running the application

* Create the database tables: <code>./bin/django syncdb</code> (create an admin user when prompted)
* Populate the database: <code>./bin/django loaddata project/db/prod.json</code>
* Start the development server: <code>./bin/django runserver</code>

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

