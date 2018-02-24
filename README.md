# Building a Github api client with django

[![Build Status](https://travis-ci.org/javierseixas/github-api-client-with-django.svg?branch=master)](https://travis-ci.org/javierseixas/github-api-client-with-django)
[![Coverage Status](https://coveralls.io/repos/github/javierseixas/github-api-client-with-django/badge.svg?branch=master)](https://coveralls.io/github/javierseixas/github-api-client-with-django?branch=master)

## Run the application



### Running with Docker

Execute the command below to start the application and its dependencies:

```
docker-compose up
```

Visit `http://localhost:8000` for overview the app.

[This tutorial](https://docs.docker.com/compose/django) from Docker was followed to set up the environment.

**NOTE**: Be sure the port 8000 is not being used in your system.


## Solution explanations

* I've used lambdas for Searcher algorithm

* DB caching should be implement using events for decoupling reasons
* Is not possible to invert order
* Ordering for results returned from cache are not ordered

## Tests

## Support

* [For configuring Pycharm with Docker](https://www.jetbrains.com/help/pycharm/configuring-remote-interpreter-via-dockercompose.html)

## TODO

* Execute migrations, in docker?
* Scenarios with api failing so cache is demostrated
* Tests
* Coverage
* Pass a PEP8 corrector