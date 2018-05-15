import os  # os.sep
import sys  # sys.exit
import stat
import time
import datetime
import traceback

import Logging

#log = Logging.Log()

class ParameterMapper():
    params = {}
    flags = {
        'mod' : ['--markofdroggo', '--mod']
    }
    optional_keywords = {
        'host_name' : ['--host']
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
        self.fill_optional()
        self.fill_flags()

    def fill(self):
        for key in self.keywords:
            missing_count = 0
            for word in self.keywords[key]:
                try:
                    index = self.argv.index(word)
                    break
                except Exception as e:
                    missing_count += 1
                    #searched through the whole list of keywords but unable to find keyword in argv
                    if missing_count == len(self.keywords[key]):
                        print("Missing Argument for " + key)
                        print(e)
                        #log.err("Missing Argument for " + key)
                        sys.exit(1)

            if key in self.params: 
                #not working
                print("Duplicate parameter for " + key)
                sys.exit(1)
            else:
                self.params[key] = self.argv[index+1]

    def fill_optional(self):
        for key in self.optional_keywords:
            found = True 
            for word in self.optional_keywords[key]:
                try:
                    index = self.argv.index(word)
                    break
                except Exception as e:
                    print(e)
                    found = False
                    
            if(found):
                if key in self.params: 
                    #not working
                    print("Duplicate parameter for " + key)
                    sys.exit(1)
                else:
                    self.params[key] = self.argv[index+1]

    def fill_flags(self):
        for key in self.flags:
            found = None 
            for word in self.flags[key]:
                if word in self.argv:
                    found = True
                    break
                else:
                    found = False
                
            if(found):
                try:
                    if key in self.params: 
                        #not working
                        print("Duplicate parameter for " + key)
                        sys.exit(1)
                    else:
                        self.params[key] = True
                except Exception as e:
                    print(e)    