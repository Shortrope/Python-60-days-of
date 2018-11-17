# Virtual Environments

    python3 -m venv venv/
    source venv/bin/activate
    deactivate

Backup and restore environment

    pip3 freeze > requirements.txt
    pip3 install -r requirements.txt

Root Proj Dir
    src/
    test/
    venv/
    .gitignore
    requirements.txt

.gitignore

    .venv
    venv/
    ENV/
