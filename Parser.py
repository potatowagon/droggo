#! python3
import os  # os.sep
import sys  # sys.exit
import stat
import time
import datetime
import traceback

import Logging

log = Logging.Log()

class ParameterMapper():
    params = {}
    options = {}
    optional_keywords = {
        'mod' : ['--markofdroggo', '--mod']
    }
    keywords = {
        'file_path' : ['--fetch'],
        'org' : ['--from'],
        'find' : ['--find'],        
        'replace' : ['--replace', '--rep'],
        'credentials' : ['-u']
    }
    argv = None

    def __init__(self, argv):
        self.argv = argv
        self.fill()

    def fill(self):
        for key in self.keywords:
            missing_count = 0
            for word in self.keywords[key]:
                try:
                    index = self.argv.index(word)
                    break
                except:
                    missing_count += 1
                    #searched through the whole list of keywords but unable to find keyword in argv
                    if missing_count == len(self.keywords[key]):
                        log.err("Missing Argument for " + key)
                        sys.exit(1)

            if key in self.params:
                log.err("Duplicate parameter for " + key)
                sys.exit(1)
            else:
                self.params[key] = self.argv[index+1]

                