# first_end_to_end_ML

steps:
1.first create virtual environment
2.activate it
3.in .gitignore write venv/ to ignore the venv
4.create a requirements.txt file to install all the packages required for the project
5.install it by using pip install -r requirements.txt
6.Now we have t0 create a template.py file to create all the necessary files at once
7.once the coding part in template.py completed then running it will get us our basic required files
8.In src/MLOPS/__int__.py we have to create a logger 
9.This loggwr will help us to log the process easily
8.in that __init__.py file we can create a logs folder in that logging.log file to save the logging info
9.create a config folder in that create a config.yaml file so  that we can specify the data download link and artifacts folder path
10.in src/MLOPS/utils/common.py create a funtion call read_yaml
