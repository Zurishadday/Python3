"""import logging
logging.basicConfig()
logging.debug("A Debug Logging Message")
logging.info("A Info Logging Message")
logging.warning("A Warning Logging Message")
#WARNING:root:A Warning Logging Message
logging.error("An Error Logging Message")
#ERROR:root:An Error Logging Message
logging.critical("A Critical Logging Message")
#CRITICAL:root:A Critical Logging Message
"""
import logging

logging.basicConfig(format='Date-Time : %(asctime)s : Line No. : %(lineno)d - %(message)s', \
                    level = logging.DEBUG)
logging.debug("A Debug Logging Message")
logging.info("A Info Logging Message")
logging.warning("A Warning Logging Message")
logging.error("An Error Logging Message")
logging.critical("A Critical Logging Message")

