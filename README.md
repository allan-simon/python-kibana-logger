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

## Usage

You can use the new_with() function to create a first set of parameters to log.

```
logger = logger.new_with({"action": "get_logs"})
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
    x_logger = logger.new_with({"api_endpoint": "get_logs"})

    # log app / stack / api_endpoint / user_id
    x_logger.info({"user_id": "a_user_id"})

    # log app / stack / api_endpoint / amount
    x_logger.info({"amount": "42"})

def bar(logger):
    """
    Second method
    """
    x_logger = logger.new_with({"request_id": uuid4()})

    # log app / stack / request_id / request_time
    x_logger.info({"request_time": "35"})

    # log app / stack / request_id / action
    x_logger.info({"action": "do_something"})

foo(logger)
bar(logger)
```
