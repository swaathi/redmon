# Redmon
Monitor a Redis key

## Installation
Redmon requires a working Redis connection.

To install Redmon from pip,
`pip install redmon`

Or from source,
`python setup.py install`

## Setup
Redmon connects to your Redis connection with the following environment variables.
If none are set, default values are used.
- REDMON_REDIS_HOST (default, `localhost`): Set it to where your Redis is running from.
- REDMON_REDIS_PORT (default, `6379`): Set it to where your Redis is running on.
- REDMON_TIME_INT (default, `1`): Set the time interval your Redis key should be refreshed at.

## Get Started
To watch a Redis key, just simply

`redmon watch --key=snapshot`

Key is the name of the Redis key you want to monitor.

## Coming Up
- Monitor multiple keys
- Set the values your Redis key should be compared against
- Set the values your Redis key should never be
- Set custom time interval for each monitor
