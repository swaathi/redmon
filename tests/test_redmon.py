# -*- encoding: utf-8 -*-
import os
import pytest
from redmon import Redmon

def test_key_not_empty():
    with pytest.raises(ValueError):
        redmon = Redmon()

# Passes when Redis connection is available
def test_redis_connection():
    redmon = Redmon("sample")
    assert isinstance(redmon, Redmon)

def test_interval_set_with_environment_variable():
    os.environ["REDMON_TIME_INT"] = "2"
    redmon = Redmon("sample")
    assert redmon.interval == 2.0

def test_interval_set_with_object_instantiation():
    redmon = Redmon("sample", interval=2)
    assert redmon.interval == 2.0

def test_do_not_compare_when_value_is_not_set():
    redmon = Redmon("sample")
    assert redmon.compare(redmon.get_redis_value())

def test_compare_when_value_is_set():
    redmon = Redmon("sample", trueval="sample")
    redmon.redis.set("sample", "sample")
    assert redmon.compare(redmon.get_redis_value())
