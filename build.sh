#!/bin/sh
#
# Builds an example application with placeholder objects
# and an admin user with username 'admin', password 'password'.
#
# Requires that a postgreSQL database has been created for the application
#
set -e # stops execution on error
rm -rf webapp/migrations
python manage.py migrate
python manage.py test