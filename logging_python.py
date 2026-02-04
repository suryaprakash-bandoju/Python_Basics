# Learn how to use Logging like a pro

# Logging Basics
#____________________________________________________________________________

import logging

# setup Logger
logging.basicConfig(level=logging.DEBUG)

# Log Message
logging.debug('This is a debug msg.')          #10
logging.info('This is a info msg.')            #20
logging.warning('This is a warning msg.')      #30
logging.error('This is a error msg.')          #40
logging.exception('This is a exception msg.')  #40 < - Includes Exception Traceback
logging.critical('This is a critical msg.')    #50

