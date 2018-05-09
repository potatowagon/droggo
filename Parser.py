#! python3
import os  # os.sep
import sys  # sys.exit
import stat
import time
import traceback
import datetime
import getopt

class ParameterMapper():
    params = {}
    keywords = {
        'file_path' : ['--fetch'],
        'org' : ['--from'],
        'find' : ['--find'],        
        'replace' : ['--replace', '--rep']
    }
    argv = None

    def __init__(self, argv):
        self.argv = argv
        self.fill()

    def fill(self)