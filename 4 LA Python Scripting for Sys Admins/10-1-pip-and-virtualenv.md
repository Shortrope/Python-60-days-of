# Pip and Virtualenv

## pip
### What is already installed?

    pip3 list

    Package             Version
    ------------------- ---------
    asn1crypto          0.24.0
    attrs               17.4.0
    Automat             0.6.0
    blinker             1.4
    certifi             2018.1.18

may need to create and edit the pip.conf file for the warning

    mkdir ~/.conf/pip/pip.conf

    [list]
    format=columns

### Get list of installed .. for reinstall file

    pip3 freeze

    asn1crypto==0.24.0
    attrs==17.4.0
    Automat==0.6.0
    blinker==1.4
    certifi==2018.1.18

### Install / Uninstall using requirements.txt file
Save the package/ver list to file

    pip3 freeze > requirements.txt
    pip3 unistall -y -r requirements.txt

Install for the user

    pip3 install --user -r requirements.txt
    /home/user/.local/lib/python3.6/...

## Virtualenv
Sandboxed environments

    mkdir venvs
    python3.6 -m venv --help
    python3.6 -m venv venvs/experiment

    ls venvs/experiment/bin

Enter the virtual environment by 'source'ing the 'activate' script

    source venvs/experiment/bin/activate
    which python
    pip list

Use full path to python in the #!

    #!/home/user/venvs/experiment/bin/python

Exit the virtual environment
    deactivate

## Using 3rd party packages 
Find packages at https://pypi.python.org/pypi

    pip3 install requests