# -*- encoding: utf-8 -*-
import os
import time

# Modules in Redmon
from conf import time_interval, get_redis, check_redis

class Redmon():
    @staticmethod
    def watch(key):
        redis = get_redis()

        if not check_redis(redis):
            print "Unable to connect to Redis!"
            return False

        print "* Watching '{0}' (Press CTRL+C to quit)".format(key)

        interval = time_interval()
        try:
            while True:
                print redis.get(key)
                time.sleep(interval)
        except KeyboardInterrupt:
            print "Not watching '{0}' anymore! Byeeee.".format(key)
