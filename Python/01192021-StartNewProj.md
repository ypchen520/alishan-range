## Steps for starting a new project
# PyCharm
* clone git repo with the target folder: TAR
* create a virtual env outside TAR
  * python3 -m venv venv/
* run ```source venv/bin/activate
* run ```pip install -r requirements.txt``` (for distribution)
* in TAR
  * run ```pip freeze > requirements.txt``` to generate the dependency file
* in PyCharm
  * File > settings > Project: PROJ_NAME > Project Interpreter > + 
  * Run > Edit Configurations
