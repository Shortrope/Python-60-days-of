# Pipenv
https://docs.pipenv.org

    pip3 install --user pipenv
    pipenv -h

Create a python3 virtual environment

    cd myapp/
    pipenv --python $(which python3)

Initialize git and create .gitignore

    git init
    curl -o .gitignore https://raw.githubusercontent.com/github/gitignore/master/Python.gitignore

Enter the virtual environment

    pipenv shell

Install into environment

    pipenv install --dev pytest
    pipenv install requests
    cat Pipfile

## Example

    pip3 install --user pipenv

    mkdir myapp
    cd myapp
    pipenv --python $(which python3)

    pipenv install --dev pytest
    pipenv install requests
    cat Pipfile

    vim main.py

    pipenv run python main.py
    or
    pipenv shell
    ./main.py