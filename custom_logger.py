import logging

logger = logging.getLogger("my_logger")

logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("debug.log")
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

logger.debug("This is a debug message from my_logger")
logger.info("This is a info message from my_logger")
logger.warning("This is a warning message from my_logger")
logger.error("This is a error message from my_logger")
logger.critical("This is a critical message from my_logger")