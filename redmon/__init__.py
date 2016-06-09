# -*- encoding: utf-8 -*-
import os
import time
from termcolor import colored

# Modules in Redmon
import conf

class Redmon():
    def __init__(self, key=None, trueval=None, interval=None):
        if key is None: raise ValueError("Key must not be empty")

        self.key = key
        self.trueval = str(trueval)
        self.redis = conf.get_redis()
        self.interval = conf.get_time_interval(interval)

    def get_redis_value(self):
        return self.redis.get(self.key)

    def monitor(self):
        print "* Watching '{0}' every {1} seconds (Press CTRL+C to quit)".format(self.key, self.interval)

        try:
            while True:
                value = self.get_redis_value()
                timestamp = time.strftime("%H:%M:%S")

                if not self.compare(value):
                    value = colored(value, 'red')

                print "{0} - {1}".format(timestamp, value)
                time.sleep(self.interval)
        except KeyboardInterrupt:
            print "\nNot watching '{0}' anymore! Byeeee.".format(self.key)

    def compare(self, value):
        if self.trueval == 'None':
            return True
        else:
            return self.trueval == value
