# Pipeline
This folder contains an ETL script that uploads match data to the database.


## Prerequisites
Make sure you have the following installed on your device:
- `python` for running the seeding script.

## Setup and Installation
- Create a `.env` file with the following format:
```bash
PLAYER_ID=XXXX
```
`PLAYER_ID` is the ID of the Dota 2 player you want to analyse.

- By creating a virtual environment first, or otherwise, install the required python libraries by running `pip install requirements.txt`.
- Run `python3 pipeline.py`.

## Files Explained
- `pipeline.py`: An ETL script that gets a player's game data from the Dota 2 API, and uploads the data to the database.


