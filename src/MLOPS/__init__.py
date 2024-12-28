import logging
import os
import sys

log_dir="logs"
log_filepath=os.path.join(log_dir,"logging.log")
os.makedirs(log_dir,exist_ok=True)

logging.basicConfig(level=logging.INFO,
    format='[%(asctime)s]: %(name)s-%(levelname)s-%(message)s:',
    datefmt='%Y-%m-%d-%H:%M:%S',

   handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
    )

#Instead of root this will give MLOPSLogger  
#  before:[2024-12-13-07:21:14]: root-INFO-custom log:
logger=logging.getLogger("MLOPS_Logger")
#  after:[2024-12-13-07:22:04]: MLOPS_Logger-INFO-custom log:

