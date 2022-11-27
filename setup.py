import os
import platform
import re
import sys
import warnings


from setuptool import find_packages, setup

def get_requirements():
    pass

setup(
    name="sensor",
    version="0.0.1",
    author="Saurav Bhalotia",
    
    # if a folder contains a file __init__.py file 
    # that implies that particular folder is a package / module / etc.
    packages= find_packages(),
    
    install_requires=get_requirements(),
)