import  logging

logging.basicConfig(filename="C:/Users/navan/OneDrive/Desktop/test.log",
                    format='%(asctime)s: %(levelname)s: %(message)s',
                  #  datefm='%m/%d/%Y  %I:%M:%S %p',
                    level=logging.DEBUG)

logging.debug("this is a debug message")
logging.info("this is an info message")

logging.warning("this is  a waringin message")
logging.error("this is error message")
logging.critical("this is a critical message")