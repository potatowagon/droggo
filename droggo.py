import os  # os.sep
import sys  # sys.exit
import stat
import time
import datetime
import traceback

import Help
import Logging
import Parser


log = Logging.Log()

def main():
    
    if len(sys.argv) < 3:
        Help.show()
        sys.exit(1)

    try:
        log.debug(sys.argv)
        parser = Parser.ParameterMapper(sys.argv)
        print(parser.params)
    except:

        sys.exit(1)

if __name__ == "__main__":
    main()
