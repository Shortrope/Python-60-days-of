# Questions
What is setup.py really all about?  
Makefile?  
README.rst?  
__init__.py  
Pipfile  
setup.py vs Pipfile dependencies  
create wheel file
why use --user in `pip install --user ...`



# Planning

# Documentation
## Python README.rst  
restructured text  
http://docutils.sourceforge.net/rst.html


        pgbackup
        ========

        CLI for backing up remote PostgreSQL databases locally or to AWS S3.

        Preparing for Development
        -------------------------

        1. Ensure ``pip`` and ``pipenv`` are installed
        2. Clone repository: ``git clone git@github.com:example/pgbackup``
        3. ``cd`` into repository
        4. Activate virtualenv: ``pipenv shell``
        5. Fetch development dependencies ``make install``

        Usage
        -----

        Pass in a full database URL, the storage driver, and destination.

        S3 Example w/ bucket name:

        ::

            $ pgbackup postgres://bob@example.com:5432/db_one --driver s3 backups

        Local Example w/ local path:

        ::

            $ pgbackup postgres://bob@example.com:5432/db_one --driver local /var/local/db_one/backups

        Running Tests
        -------------

        Run tests locally using ``make`` if virtualenv is active:

        ::

            $ make

        If virtualenv isn’t active then use:

        ::

            $ pipenv run make
        ~                                            


## Directory Structure
code/pgbackup
    src/
        pgbackup/
            __init.py__
    tests/
        .gitkeep


## Setuptools - Building and Distributing Packages
Very important!  
https://setuptools.readthedocs.io/en/latest/setuptools.html#basic-use  

_setup.py_

Enter the virtual environment and run `pip install` so it will use the setup.py file to install the 'program' and dependencies - 'pgbackup' in this case.

    pip install -e .

Uninstall with

    pip uninstall pgbackup

## Make file - Run some tasks
https://www.gnu.org/software/make/manual/make.html  

Makefile

    .PHONY: install test

    default: test

    install:
            pipenv install --dev --skip-lock

    test:
            PYTHONPATH=./src pytest

The Makefile will make files based on the task name, 'install' and 'test'  
The '.PHONY:' line tells it not to create files for the designated tasks  
Running `make` by itself will run the 'default'.

# TDD
RED > Green > Refactor  
Install 'pytest'  
https://docs.pytest.org/en/latest/  

    pipenv install --dev pytest

Fixtures look cool!  

Write separate test module (file) for different 'domains' or parts of the application.  
- argument parsing
- database interactions
- presentation


## Mocking in Tests
https://github.com/pytest-dev/pytest-mock/#usage

    pipenv install --dev pytest-mock

### Mock running `pg-dump`
We will only test that the command is sent properly  

    def test_dump_calls_pg_dump(mocker):
        """
        Utilize pg_dump with the database URL
        """
        mocker.patch('subprocess.Popen')
        assert pgdump.dump(url)
        
Test that pg_dump exists else throws error

    def test_dump_handles_os_error(mocker):
        """
        pgdump.dump returns a reasonalbe error if pg_dump insn't installed
        """
        mocker.patch('subprocess.Popen', side_effect=OSError('no shuch file'))
        with pytest.raises(SystemExit):
            pgdump.dump(url)
        subprocess.Popen.assert_called_with(['pg_dump', url], stdout=subprocess.PIPE)


