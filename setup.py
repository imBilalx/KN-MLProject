from typing import List
from setuptools import find_packages, setup

HYPHEN_E_DOT = '-e .'


def get_requirements(file_path: str) -> List[str]:
    """
    Read requirements from file
    :param file_path:
    :return: List of requirements
    """
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n', '') for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

        return requirements


setup(
    name='KN-MLProject',
    version='0.0.1',
    author='Bilal Akhtar',
    author_email='bilalakhtar268@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
