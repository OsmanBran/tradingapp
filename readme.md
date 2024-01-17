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

to connect locally
`pipenv run python -m websockets ws://localhost:8765/ -m websockets ws://localhost:8765/`

## Trouble shoot python env
check your local pipenv running
- run `pipenv shell`

check your vs code running pipenv
- ctrl shift P select python interpreter (pyshell)

## After changing your python env.
1. remove old python paths from system variables and restart
2. pipenv --rm to delete old files from pipenv
3. pipenv --python <NEW_VERSION>
4. pipenv install should now work.
