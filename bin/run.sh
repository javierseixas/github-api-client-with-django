#!/bin/sh
#
# Builds an example application with placeholder objects
# and an admin user with username 'admin', password 'password'.
#
# Requires that a postgreSQL database has been created for the application
#
set -e # stops execution on error
python3 manage.py migrate
python3 manage.py runserver 0.0.0.0:8000