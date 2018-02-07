import logging,os
import argparse

##### argument parser revises. Not necessary.
parser = argparse.ArgumentParser(prog="a simple logger", description="console debug level is set by argument parser or DEBUG by default")

arg_group_log = parser.add_mutually_exclusive_group()
arg_group_log.add_argument('-i', '--info', action='store_true')  # INFO
arg_group_log.add_argument('-d', '--debug', action='store_true')    # DEBUG
arg_group_log.add_argument('-e', '--error', action='store_true')    # ERROR
                                                                    # DEFAULT IS WARNING

args = parser.parse_args()
# initialize a logger
logger = logging.getLogger('logger')
"""
Loggers that are further down in the hierarchical list are children of loggers higher up in the list.
like `logger.second`
"""
logger.propagate = True
seclogger = logging.getLogger('logger.second')
seclogger.propagate = True  #  Messages are passed directly to the ancestor loggers’ handlers

logger.setLevel(logging.DEBUG)
seclogger.setLevel(logging.INFO)
seclogger.isEnabledFor(logging.DEBUG)
print(logger.getEffectiveLevel())  # print current logger towards the root setting      10 DEBUG
print(seclogger.getEffectiveLevel())    # 20
print(logger.getChild('second').getEffectiveLevel())   # return seclogger

fmt = '[%(asctime)s %(levelname)s] @%(name)s | %(message)s'
formatter = logging.Formatter(fmt, datefmt='%Y.%m.%d %H:%M:%S')

FILE_LOG = os.path.join(os.getcwd(), 'log.txt')

# add handler to FILE_LOG in working directory
handler_file = logging.FileHandler(FILE_LOG, mode='w')

handler_file.setFormatter(formatter)
handler_file.setLevel(logging.NOTSET)
logger.addHandler(handler_file)
#   add handler to console


handler_console = logging.StreamHandler()
## parser setting
if args.info:
    handler_console.setLevel(logging.INFO)
elif args.debug:
    handler_console.setLevel(logging.DEBUG)
elif args.error:
    handler_console.setLevel(logging.ERROR)
else:
    handler_console.setLevel(logging.WARNING)

handler_console.setFormatter(formatter)
# handler_console.setLevel(logging.WARNING)
logger.addHandler(handler_console)


# demo
logger.info("Initializing a logger")
seclogger.info("Initializing a second logger")

logger.warning( "WARNING msg written to file")
logger.debug(   "DEBUG   msg written to file")
logger.error(   "ERRORS  msg written to file")
seclogger.warning("second logger is writing a warning")
# logger debug level
"""
 .warning(msg, *args, **kwargs)#
 .info(msg, *args, **kwargs)
 .error(msg, *args, **kwargs)
 .critical(msg, *args, **kwargs)
 .log(lvl, msg, *args, **kwargs)
 .exception(msg, *args, **kwargs)
"""


# logger filter
"""
 .addFilter(filter)
 .removeFilter(filter)
 .filter(record)
 .addHandler(hdlr)
 .removeHandler(hdlr)
 .findCaller(stack_info=False)
 .handle(record)
 .makeRecord(name, lvl, fn, lno, msg, args, exc_info, func=None, extra=None, sinfo=None)
 .hasHandlers()
"""

# Logging Levels
"""
CRITICAL	50
ERROR	40
WARNING	30
INFO	20
DEBUG	10
NOTSET	0
"""

# Handler object
