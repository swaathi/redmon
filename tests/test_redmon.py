# -*- encoding: utf-8 -*-
from redmon import Redmon

def test_redis_connection():
    redmon = Redmon()
    assert isinstance(redmon, Redmon)
