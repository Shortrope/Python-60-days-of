# Tips and Tricks

## Virtual environments
You can create isolated Python environments  
These can have different versions of python or other packages

    pip3 install virtualenv

From a terminal / PowerShell

    virtualenv <env_name>
    virtualenv pluralsight
    virtualenv --python=python3.7 pluralsight

This creates a Directory w many subfolders  
You can keep all your virtual environment in the same location

    /home/mario/venvs

To start an environment

    source /home/mario/venvs/pluralsight/bin/activate

Any packages installed in the environment stay in that env.  
To Stop the environment  

    deactivate
