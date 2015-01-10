import logging
import logging.config
logging.config.fileConfig('logger.conf')

# create logger
logger = logging.getLogger(__name__)

def say():
	logger.debug('debug message')
	logger.info('info message')
	logger.warn('warn message')
	logger.error('error message')
	logger.critical('critical message')
	print 'hi'