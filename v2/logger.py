import logging

class Logger():

    def __init__(self):
        self.info("Logging facility starting")

    def debug(self, message):
        print ("DEBUG :: %s" % message)

    def info(self, message):
        print ("INFO :: %s" % message)

    def warn(self, message):
        print ("WARNING:: %s" % message)

    def err(self, message):
        print ("ERROR:: %s" % message)



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