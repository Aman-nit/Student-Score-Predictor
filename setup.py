''' It is required to create a package of your project and if i upload it in pypi it can be used by anyone as we are using tha packageds like pandas, numpy ... etc , Just by installing it using pip install "Packagename" '''

from setuptools import find_packages,setup
from typing import List

def get_requirments(file_path:str)->list[str]:
    '''  This is the function which provide list of the requirments  to install for making package from "requirments.txt" '''
    HYPEN_E_DOT = '-e .'
    requirments= [] #list of the strings
    with open(file_path) as file_obj: # this will open the requirments.txt as a file_obj
        requirments = file_obj.readlines() # this will read the each line 
        requirments =[req.replace("\n","")for req in requirments]

        if HYPEN_E_DOT in requirments:
            requirments.remove(HYPEN_E_DOT)

    return requirments


setup(
    name="Mlproject",
    version='0.0.1',
    author='Aman',
    author_email='aman.nit.cse@gmail.com',
    packages=find_packages(),
    install_requires= get_requirments('requirments.txt')
)