from setuptools import find_packages, setup
from typing import List

al = '-e .'
def get_req(file_path:str)->List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements = [_.replace('\n','') for _ in requirements]
        if al in requirements:
            requirements.remove(al)
    return requirements

setup(
    name='h501',
    version='1.0',
    author='Alvin',
    author_email='ahampto@iu.edu',
    packages=find_packages(),
    install_requires=get_req('requirements.txt')
)