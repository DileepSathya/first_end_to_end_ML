import logging
import os
logging.basicConfig(level=logging.INFO,
    format='[%(asctime)s]: %(name)s-%(levelname)s-%(message)s:',
    datefmt='%Y-%m-%d-%H:%M:%S',
    filename='logs/logger.py',
    filemode='w'
    )
logging.info("hi")

