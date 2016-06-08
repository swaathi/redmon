# -*- encoding: utf-8 -*-
import os
import redis
# redis = redis.StrictRedis(host='localhost', port=6379, db=0)

# Get Time Interval
def get_time_interval(time=None):
    interval = time or get_env_var("REDMON_TIME_INT", 1.0)
    interval = float(interval)
    if (interval < 0.05):
        interval = 1.0

    return interval

# Get Redis connection
def get_redis():
    host = get_env_var("REDMON_REDIS_HOST", 'localhost')
    port = get_env_var("REDMON_REDIS_PORT", 6379)
    re = redis.StrictRedis(host=host, port=port, db=0)

    # Checking if Redis successfully connected
    if check_redis_connection(re):
        return re

# Check if Redis is connected
def check_redis_connection(re):
    try:
        response = re.client_list()
        return True
    except:
        raise RedisConnectionError("Unable to connect to Redis!")

# Get environment variable or return default value
def get_env_var(var, default):
    try:
        env_var = os.environ[var]
        return env_var
    except:
        return default

class RedisConnectionError(Exception):
    def __init__(self,*args,**kwargs):
        Exception.__init__(self,*args,**kwargs)
