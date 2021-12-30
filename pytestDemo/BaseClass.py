import logging


class BaseClass:

    def getlogger(self):
        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
        fileHandler = logging.FileHandler('logfile.log')
        fileHandler.setFormatter(formatter)
        logger = logging.getLogger(__name__)
        logger.addHandler(fileHandler)  # pass File Handler object in it

        logger.setLevel(logging.INFO)
        return logger