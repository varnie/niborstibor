### Setup virtual environment and install project dependencies:
    python -m venv venv
    source venv/bin/activate

### Help
    source venv/bin/activate
    python ./src/app.py

### Initial Nibor import:
    source venv/bin/activate
    python ./src/app.py --name=nibor --action=initial_import


### Run demon for fetching Nibor upcoming data:
    source venv/bin/activate
    cd src
    python ./src/app.py --name=nibor --action=daemon


### Initial Stibor import:
    source venv/bin/activate
    cd src
    python ./src/app.py --name=stibor --action=initial_import


### Run demon for fetching Stibor upcoming data:
    source venv/bin/activate
    cd src
    python ./src/app.py --name=stibor --action=daemon