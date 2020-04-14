# https://docs.python.org/3/howto/logging.html#logging-to-a-file
import logging
logging.basicConfig(filename='02-example.log',level=logging.DEBUG)
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')
