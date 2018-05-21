import os  # os.sep
import sys  # sys.exit
import stat
import time
import datetime
import traceback

import Help
import Logging
import Parser
import Command


log = Logging.Log()

def main():
    
    if len(sys.argv) < 3:
        Help.show()
        sys.exit(1)

    try:
        parser = Parser.ParameterMapper(sys.argv)
        command = Command.Command(parser.params)
        command.execute()

    except Exception as e:
        print(e)
        sys.exit(1)

    finally:
        log.__del__()

if __name__ == "__main__":
    main()
