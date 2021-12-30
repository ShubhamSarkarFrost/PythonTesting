import logging


def test_logging():
     formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
     fileHandler = logging.FileHandler('logfile.log')
     fileHandler.setFormatter(formatter)
     logger = logging.getLogger(__name__)
     logger.addHandler(fileHandler)  # pass File Handler object in it

     logger.setLevel(logging.INFO)
     logger.debug("A debug statement is executed :")
     logger.info("Information statement")
     logger.warning("Something is in Warning Mode")
     logger.error("Error Encountered")
     logger.critical("You are Fucked badly !!")

     return logger
