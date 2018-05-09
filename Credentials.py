import re

class Credentials():
    username = None
    password = None

    def __init__(self, str):
        str = str.strip()
        if is_valid(str):
            str = str.split(':')
            self.username = str[0]
            self.password = str[1]
            
def is_valid(str):
    valid = re.match(r'\w+:\w+', str)
    return valid