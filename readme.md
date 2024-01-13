trading bot for btc markets

## Install
pipenv install

To activate this project's virtualenv, run pipenv shell.
Alternatively, run a command inside the virtualenv with pipenv run.

## Download BackTest Data
1. Download Mongo DB community server and boot up on local host
2. Set BacktestDb variables with appropriate interval time etc.
3. Run the download script
`pipenv run python  src/BacktestDb.py`

## Run Server
`pipenv run python src/Server.py`

## Trouble shoot python env
check your local pipenv running
- run `pipenv shell`

check your vs code running pipenv
- ctrl shift P select python interpreter (pyshell)