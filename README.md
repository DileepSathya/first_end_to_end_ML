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
8.in that __init__.py file we can create a logs folder by calling a create file
9.which will call the function create_file function in src/MLOPS/utils/common.py
10.this function will create logs folder and logging.log file this logging.log file is will save our loggings
11.to create logs folder as mentioned below i created a params/params.yaml(modified in emplate .py) from that i will create the logs/logging.log file
12.