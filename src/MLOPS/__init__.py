import logging
import os
logging.basicConfig(level=logging.INFO,
    format='[%(asctime)s]: %(name)s-%(levelname)s-%(message)s:',
    datefmt='%Y-%m-%d-%H:%M:%S',
    
    )

#Instead of root this will give MLOPSLogger  
#  before:[2024-12-13-07:21:14]: root-INFO-custom log:
logger=logging.getLogger("MLOPS_Logger")
#  after:[2024-12-13-07:22:04]: MLOPS_Logger-INFO-custom log:

