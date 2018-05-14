import re
import Logging

#log = Logging.Log()

class Credentials():
    username = None
    password = None

    def __init__(self, str):
        str = str.strip()
        if 1:#is_valid(str):
            str = str.split(':')
            self.username = str[0]
            self.password = str[1]
        else:
            #log.err("Invalid Credentials")
            print("Invalid Credentials")
            
def is_valid(str):
    valid = re.match(r'\w+:\w+', str)
    return valid