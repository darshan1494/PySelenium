# Logging means -You can add logs to the failure , Information, Error ...
# It is also used to give Warning to the users

import logging
# from lib2to3.pgen2 import driver

def  test_print_logs():
    LOGGER = logging.getLogger(__name__)
    # driver.get("https://www.google.com")
    # These are intentional Logging to user
    LOGGER.info('This is information logs')
    LOGGER.warning('This is Warning logs')
    LOGGER.error('This is Error logs')
    LOGGER.critical('This is Critical logs')
    LOGGER.info('eggs info')
    LOGGER.warning('eggs warning')
    LOGGER.error('eggs error')
    LOGGER.critical('eggs critical')
