# -*- encoding: utf-8 -*-
import os
from redmon import Redmon

def test_redis_connection():
    redmon = Redmon()
    assert isinstance(redmon, Redmon)

def test_interval_set_with_environment_variable():
    os.environ["REDMON_TIME_INT"] = "2"
    redmon = Redmon()
    assert redmon.interval == 2.0

def test_interval_set_with_object_instantiation():
    redmon = Redmon(2)
    assert redmon.interval == 2.0
