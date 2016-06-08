# -*- encoding: utf-8 -*-
import os
import time

# Modules in Redmon
from conf import get_time_interval, get_redis

class Redmon():
    def __init__(self):
        self.redis = get_redis()
        self.interval = get_time_interval()

    def monitor(self, key):
        print "* Watching '{0}' (Press CTRL+C to quit)".format(key)

        try:
            while True:
                print self.redis.get(key)
                time.sleep(self.interval)
        except KeyboardInterrupt:
            print "\nNot watching '{0}' anymore! Byeeee.".format(key)
