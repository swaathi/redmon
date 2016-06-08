# -*- encoding: utf-8 -*-
import os
import time

# Modules in Redmon
import conf

class Redmon():
    def __init__(self, interval=None):
        self.redis = conf.get_redis()
        self.interval = conf.get_time_interval(interval)

    def monitor(self, key):
        print "* Watching '{0}' every {1} seconds (Press CTRL+C to quit)".format(key, self.interval)

        try:
            while True:
                print self.redis.get(key)
                time.sleep(self.interval)
        except KeyboardInterrupt:
            print "\nNot watching '{0}' anymore! Byeeee.".format(key)
