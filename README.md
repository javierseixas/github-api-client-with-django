# Building a Github api client with django

## Run the application



### Running with Docker

Execute the command below to start the application and its dependencies:

```
docker-compose up
```

Visit `http://localhost:8000` for overview the app.

[This tutorial](https://docs.docker.com/compose/django) from Docker was followed to set up the environment.

**NOTE**: Be sure the port 8000 is not being used in your system.


## Support

* [For configuring Pycharm with Docker](https://www.jetbrains.com/help/pycharm/configuring-remote-interpreter-via-dockercompose.html)

## TODO

* Switch direction of ordering
    * Maintain querystrings in order options
* Execute migrations, in docker?
* Travis
* Scenarios with api failing so cache is demostrated
* Handling errors
* Tests
* Pass a PEP8 corrector