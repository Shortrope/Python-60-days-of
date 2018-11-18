# Packaging
Make your software more accessable to others

File: _setup.py_  
Run this file to perform the installation  
Put this file at the top of your dir structure  

    from distutils.core import setup

    setup(
        name = 'palindrome',
        version = '1.0',
        py_modules = ['palindrome'],

        # metadata
        author = 'Mario Kaack',
        author_email = 'mario@mario.com',
        description = 'finds palindrom integers',
        license = 'Public domain',
        keywords = 'example'
    )

Create a vEnv in the project directory

    python3 -m venv venv/
    source venv/bin/activate

Install the module into the vEnv

    python3 setup.py install

_copying build/lib/palindrome.py -> .../venv/lib/python3.6/site-packages_

Check by cd'ing outside the proj dir and enter the REPL

    >>> import palindrome
    >>> palindrome.__file__

## Create differnt distribution formats
Takes all your modules and bundles into a distributable package

    python3 setup.py sdist --help-formats
    python3 setup.py sdist --format zip

This creates a new 'dist' dir w the distribution file.
Unzip the file - includes the src files and 'setup.py'
Run setup.py to install it into another system

Help

    python3 setup.py --help

## Install 3rd party code into your installation
- distutils
- easy_install
- pip

### distutils

    python setup.py install

### easy_install
Searches for packages in a central repo, the python index - `pypi`  
Downloads the packages w their dependencies  
[pypi.python.org/pypi](pypi.python.org/pypi)

Install easy_install  
Enter the vEnv and run

    wget http://python-distribute.org/distribute_setup.py
    python3 distribute_setup.py

Now you can install other software

    easy_install <package name>
    easy_install eagertools

Now you can import 'eagertools' into your modules or the REPL

### pip

    easy_install pip
    pip install <package name>
    pip install nose
