# PGBackup Project Steps

## 1. Create Directory Structure

    code/pgbackup
        src/
            pgbackup/
                __init.py__
        tests/
            .gitkeep

## 2. Install and enter virtual environment

    pip3 install --user pipenv

    mkdir myapp
    cd myapp
    pipenv --python $(which python3)

    pipenv shell

## 3. Create a _setup.py_ file
_setup.py_ is a requirement for an installable Python package.  
Place this file at the root fo the project directory structure.  
_setuptools_ is used to specify how our project is to be installed and define its metadata.  

### 3.1 the setup.py file
_code/pgbackup/setup.py_

    from setuptools import setup, find_packages

    with open('README.rst', encoding='UTF-8') as f:
        readme = f.read()

    setup(
        name='pgbackup',
        version='0.1.0',
        description='Database backups locally or to AWS S3.',
        long_description=readme,
        author='Keith',
        author_email='keith@linuxacademy.com',
        packages=find_packages('src'),
        package_dir={'': 'src'},
        install_requires=[]
    )

### 3.2 Intsall the package as a development package using pip

    cd code/pgbackup/
    pip install -e .

#### 3.2.1 Uninstall pgbackup package since it does nothing yet

    pip uninstall pgbackup

## 4. Makefile
Used to define tasks...  
task 1: setup the virtualenv and install dependencies w pipenv
task 2: run tests

_code/pgbackup/Makefile_

    .PHONY: default install test

    default: test

    install:
        pipenv install --dev --skip-lock

    test:
        PYTHONPATH=./src pytest

## 5. Make initial Git commit

    create .gitigore
    git add .
    git commit

## 6. Create cli API Tests
Install pytest into the venv

    pipenv install --dev pytest

## 7. Implement cli API 
## 8. Mocks for pg-dump

    pipenv install --dev pytest-mock

## 9. Implement pgbackup.dump
## 10. Tests for bgbackup.storage.local
## 11. Implement bgbackup.storage.local
## 12. Install boto3 for s3 connections
boto3 is an application dependency, so no --dev option

    pipenv install boto3

## 12. Tests for bgbackup.storage.s3
Using `mocker.Mock()`

    client = mocker.Mock()
    storage.s3(client, infile, "bucket", "file-name")
    client.upload_fileobj.assert_called_with(infile, "bucket", "file-name")

## 13. Implement bgbackup.storage.s3


## 14. Wiring the Units together
### 14.1. Add a main() function to cli.py
### 14.2. Edit setup.py
Add requirements - boto3

    install_requires=['boto3']

Add Automatic script  
https://setuptools.readthedocs.io/en/latest/setuptools.html#automatic-script-creation

    entry_points={
        'console_scripts': [
            'pgbackup=pgbackup.cli:main'
        ]
    }

## 15. Create a wheel for distribution
https://wheel.readthedocs.io/en/stable/#defining-the-python-version  

create setup.cfg

    [bdist_wheel]
    python-tag = py36

Build the 'wheel'

    python setup.py bdist_wheel

this creates a ./dist/ directory containing a .whl file
Install the wheel file with

    pip install pgbackup-0.1.0-py36-none-any.whl

This does the same thing as `pip install -e .`