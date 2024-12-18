import logging
import os

class LogGen():
    @staticmethod 
    def loggen():
        #path=os.path.abspath(os.curdir)+'\\logs\\automation.log'
        path=r"C:\\Users\\Nagalakshmi S\\Desktop\\Bix\\bbsAutomation\\logs\\automation.log"
        logging.basicConfig(filename=path,
                            format='%(asctime)s:%(levelname)s:%(message)s',
                            datefmt='%m/%d/%y %I:%M: %p', force=True)
        logger=logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger