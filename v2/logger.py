import logging
import datetime

class Logger():

    def __init__(self):
        self.info("Logging facility starting")

    def get_timestamp(self):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
        return timestamp

    def debug(self, message):
        print ("DEBUG :: %s :: %s" % (self.get_timestamp(), message))

    def info(self, message):
        print ("INFO :: %s :: %s" % (self.get_timestamp(), message))

    def warn(self, message):
        print ("WARNING :: %s :: %s" % (self.get_timestamp(), message))

    def err(self, message):
        print ("ERROR :: %s :: %s" % (self.get_timestamp(), message))

# logger = logging.getLogger(__name__)
# logger.setLevel(logging.DEBUG)
#
# LOGFILE = "logfile.log"
# FORMAT = '%(asctime)s :: %(levelname)s :: %(name)s :: %(message)s'
#
# file_handler = logging.FileHandler(LOGFILE)
# formatter = logging.Formatter(FORMAT)
# file_handler.setFormatter(formatter)
# logger.addHandler(file_handler)
#
# # Logs
# logger.debug('A debug message')
# logger.info('An info message')
# logger.warning('Something is not right.')
# logger.error('A Major error has happened.')
# logger.critical('Fatal error. Cannot continue')