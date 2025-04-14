from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
    name='Fraud Transaction Detection',
    version='0.1.0', 
    author='Siddhi',
    author_email='rawoolsiddhi814@gmail.com',
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=get_requirements('requirements.txt'),
    description='A project for detecting fraudulent transactions',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/rawoolsiddhi/fraud_transaction_detection',  
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    python_requires='>=3.8',
)
