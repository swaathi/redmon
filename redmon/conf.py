# -*- encoding: utf-8 -*-
import os
import redis
# redis = redis.StrictRedis(host='localhost', port=6379, db=0)

# Time Interval
def time_interval():
    interval = get_env_var("REDMON_TIME_INT", 1)
    if (interval < 0.05):
        interval = 1

    return interval

# Get Redis connection
def get_redis():
    host = get_env_var("REDMON_REDIS_HOST", 'localhost')
    port = get_env_var("REDMON_REDIS_PORT", 6379)
    return redis.StrictRedis(host=host, port=port, db=0)

# Check if Redis is connected
def check_redis(redis):
    try:
        response = redis.client_list()
        return True
    except:
        return False

def get_env_var(var, default):
    try:
        env_var = os.environ[var]
        return env_var
    except:
        return default
