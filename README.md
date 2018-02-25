# Building a Github api client with django

[![Build Status](https://travis-ci.org/javierseixas/github-api-client-with-django.svg?branch=master)](https://travis-ci.org/javierseixas/github-api-client-with-django)
[![Coverage Status](https://coveralls.io/repos/github/javierseixas/github-api-client-with-django/badge.svg?branch=master)](https://coveralls.io/github/javierseixas/github-api-client-with-django?branch=master)

## Run the application

You can run the application with docker or without it. In the last case, you'll need a postgres db up. In both cases, you can visit the site at [localhost:8000](http://localhost:8000).

### Running with Docker (Recommendable)

Execute the command below to start the application and its dependencies:

```
docker-compose up
```

Visit [localhost:8000](http://localhost:8000) for overview the app.

[This tutorial](https://docs.docker.com/compose/django) from Docker was followed to set up the environment.

**NOTE**: Be sure the port 8000 is not being used in your system.


### Running WITHOUT Docker

Make sure you have a postgres database. You'll probably need to change [database default config](https://github.com/javierseixas/github-api-client-with-django/blob/master/djangogithubapiclient/settings.py#L78).

Run the command below:

```
./bin/run.sh
```

Visit [localhost:8000](http://localhost:8000) for overview the app.


## Solution explanations

* **Migrations**: Used migrations utility for database changes.
* **DB Model**: Two tables are implemented:
    * Repo: Three fields for all information required. `name` is PK because is no repeatable for the required scenarios.
    * Stats: Is a table with a unique row where is stored the last request of the Api? The name of the stat is also the PK.
* **PEP 8**: Passed Pycharm PEP 8 inspection.
* **forms**: Only one form is used for the search feature.
* **Unit tests**:
* **Coverage**: `coverage` library is used, and Coveralls service is applied for easy coverage report viewing [![Coverage Status](https://coveralls.io/repos/github/javierseixas/github-api-client-with-django/badge.svg?branch=master)](https://coveralls.io/github/javierseixas/github-api-client-with-django?branch=master)
* **urls.py**: Two endpoints are implemented. One for each action of the user: List all repos, and search by name. Common templates and services are reused for each action.

### Other design explanations

* I've used lambdas for Searcher algorithm
* DB caching should be implement using events for decoupling reasons. This exists 

### Features NOT implemented

* Is not possible to invert order in list
* Ordering for results returned from cache are not ordered

## Tests

## Support

* [For configuring Pycharm with Docker](https://www.jetbrains.com/help/pycharm/configuring-remote-interpreter-via-dockercompose.html)

## TODO

* Execute migrations, in docker?
* Scenarios with api failing so cache is demostrated
* Tests
* Pass a PEP8 corrector