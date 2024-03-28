# Programming and Scripting - Week 9
# Demonstrate logging
# Based on week 9 lectures by Andrew Beatty
# Author: Ermelinda Qejvani

# Attributes you can put in the basicConfig
#   level
#   filename
#   filemode
#   format
#       %(name)s - %(levelname)s - %(message)s - %(asctime)s - (lineno)d

import logging 
logging.basicConfig(filename="./mainlog.log",
                    level=logging.DEBUG,
                    format="%(asctime)s-%(levelname)s-%(message)s-(lineno)d"  )

# prog does stuff
logging.debug("we are doing stuff")
logging.info("this is information")
logging.warning("oooohhh I am not certain about this")
logging.error("not good")
logging.critical("really bad")
