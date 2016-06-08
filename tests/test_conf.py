# -*- encoding: utf-8 -*-
import os
from redmon import conf

def test_redis_connection():
    redis = conf.get_redis()
    assert redis != False

def test_minimum_time_interval():
    os.environ["REDMON_TIME_INT"] = "0.005"
    min_interval = conf.get_time_interval()
    assert min_interval == 1

def test_default_environment_variable_values():
    host = conf.get_env_var("REDMON_REDIS_HOST", 'localhost')
    assert host == 'localhost'
