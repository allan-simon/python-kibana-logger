# python-kibana-logger

[![PyPI version](https://badge.fury.io/py/kibana-logger.svg)](https://badge.fury.io/py/kibana-logger)

Module to ease logging in json format that can be later displayed in Kibana.



## Installation

```
pip install kibana_logger
```

## Initialization

Create the main logger instance :

```python
logger = KibanaLogger({"app": "your_app_name"})
```


## Configuratiopn

You can configure the log level using the ENV variable `KIBANA_LOGGER_LOG_LEVEL`:
* DEBUG
* INFO (default)
* WARNING
* ERROR

## Create a new instance

You can use the `clone_with()` function to create a first set of parameters to log.

```
logger = logger.clone_with({"action": "get_logs"})
```

Note: there's a `new_with` function that does exactly the same thing but
it is deprecatd as it was not obvious to people that it was returning
a new instance and NOT updating the current version

## Add a new set of parameters

You can use the `update_in_place()` function add a new set of parameters to the current logger instance.

```
logger.update_in_place({"resource_id": "0"})
```

## Log information

There are different kind of logs that will be written into syslog
( info, error, warning... etc... ).

Example of log action:

```python
logger.info({"api_call": "called_action_name"})
```

## Full example

```python
"""
Kibana logger usage example
"""

logger = KibanaLogger(
    {
        "app": "my_app",
        "stack": "my_stack"
    }
)

logger.info({"message": "my message"})

def foo(logger):
    """
    First method
    """
    x_logger = logger.clone_with({"api_endpoint": "get_logs"})

    # it will log the tags:
    # app / stack / api_endpoint / user_id
    x_logger.info({"user_id": "a_user_id"})
    
    # it will log the tags:
    # app / stack / user_id
    # NOTE logger. was not updated !
    logger.info({"user_id": "a_user_id"})

    # it will log the tags:
    # log app / stack / api_endpoint / amount
    x_logger.info({"amount": "42"})

def bar(logger):
    """
    Second method
    """
    x_logger = logger.clone_with({"request_id": uuid4()})

    # log app / stack / request_id / request_time
    x_logger.info({"request_time": "35"})

    # log app / stack / request_id / action
    x_logger.info({"action": "do_something"})

def update_logger_default_set(logger):
    """
    Update the logger instance by adding a new parameter set
    """
    logger.update_in_place({"resource_id": "0"}


def baz(logger):
    """
    Third method
    """
    # log app / stack / step
    x_logger.info({"step": "start"})
    
    # Call the function that add "resource_id" to the logger parameter set
    update_logger_default_set(logger)
    
    # log app / stack / resource_id / step
    x_logger.info({"step": "end"})

foo(logger)
bar(logger)
baz(logger)
```
