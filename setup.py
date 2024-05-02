from setuptools import setup, find_packages

def load_requirements(filename='requirements.txt'):
    with open(filename, 'r') as f:
        requirements = f.read().splitlines()
    return requirements

setup(
    name='TLS-Mimic',
    version='0.1',
    packages=find_packages(),
    install_requires=load_requirements()
)