import sys  # sys.stdout, sys.stderr
import datetime  # datetime.datetime.now, datetime.timedelta (implicit)


# A Singleton type class to be used for logging of all types
class Log():
    # Class variables (shared across instances)
    outstream = sys.stdout  # Standard output stream (info + debug)
    logstream = None  # Standard output stream (info + debug)
    errstream = sys.stderr  # Standard error stream (error + warning)

    silent = False  # Flag for enabling or disabling output stream
    dev = False  # Flag for enabling or disabling debug

    timestamps = {}  # Dictionary for tracking of time

    # Creates logstream if necessary
    def __init__(self):
        if Log.logstream is None:
            Log.logstream = open("droggolog.txt", "a")

    # Closes logstream
    def __del__(self):
        if Log.logstream is not None:
            Log.logstream.close()
        Log.logstream = None

    # Prints to both outstream and logstream
    def log(self, stream, text=""):
        print >> stream, text
        print >> Log.logstream, text

    # Logs info text to outstream
    # e.g. Current step in pipeline
    def info(self, text=""):
        if not Log.silent and text:
            self.log(Log.outstream, "Droggo Log: " + str(text))

    # Logs debug text to outstream
    # e.g. Current value of object
    def debug(self, text=""):
        if Log.dev and text:
            self.log(Log.outstream, "Droggo Debug: " + str(text))

    # Logs timestamped info text to outstream
    def stamp(self, text="", key=None):
        timestamp = datetime.datetime.now()  # Get current timestamp
        timedelta = None  # Time delta to be calculated if possible

        # If a key is given, check whether it is being tracked
        if key is not None:
            if Log.timestamps.keys().__contains__(key):
                timedelta = timestamp - self.timestamps[key]
            # Update the timestamp for this key
            Log.timestamps[key] = timestamp

        if not Log.silent:
            self.log(Log.outstream, "Droggo Time-stamped Log: {} {}".format(
                "[{}]".format(timestamp), str(text)))

        # Returns None if no key is specified, or if it was not calculable
        return timedelta

    # Logs error text to errstream
    # e.g. Error occurred during execution
    def err(self, text=""):
        if text:
            self.log(Log.errstream, "Droggo Error: " + str(text))


# A base class for all classes that require logging
class Loggable():
    # All loggable objects must have a name
    def name(self):
        return "Droggo Object: {}".format(self.__class__.__name__)

    # All loggable objects must be convertable to string
    def __str__(self):
        return self.name()
