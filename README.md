[![Codacy Badge](https://api.codacy.com/project/badge/Grade/b9b2abf80de34584a596147b099f4473)](https://app.codacy.com/gh/gabrielsr/standalone-smach?utm_source=github.com&utm_medium=referral&utm_content=gabrielsr/standalone-smach&utm_campaign=Badge_Grade_Settings)
[![Build Status](https://travis-ci.org/gabrielsr/standalone-smach.svg?branch=master)](https://travis-ci.org/gabrielsr/standalone-smach)
[![codecov](https://codecov.io/gh/gabrielsr/standalone-smach/branch/master/graph/badge.svg)](https://codecov.io/gh/gabrielsr/standalone-smach)


Ros SMACH fork for development of HSM outside of ROS
======================================================

Fork of ros smach with the objective to make it easy to test HSM.



Test
----

Tests should be put on /tests folder and are executed with the following command.

```console
 $ pytest -v --cov .
```

Linter
------

```console
 $ flake8 --statistics
```

Dependency
----------

Add New Dependency
------------------

To add new dependencies use the following command.

```console
$ pipenv install [name]
```

This command will add the dependency to the Pipfile and Pipfile.lock assuring that the execution can be reproduced in another environment (after dependencies are updated with `pipenv install` command )

Add New Dev Dependency
----------------------
Same as previous dependencies, but for development libraries such as the ones used for test.

```console
$ pipenv install [name] --dev
```
Note that other systems after pulling updates will need a reexecution of `pipenv install --dev`
