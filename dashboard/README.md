# Dashboard
This folder contains scripts that create the analytics dashboard.


## Prerequisites
Make sure you have the following installed on your device:
- `python` for running the seeding script.

## Setup and Installation
- Create a `.env` file with the following format:
```bash
PLAYER_NAME=XXXX
PLAYER_AVATAR=XXXX
```
`PLAYER_NAME` is the steam tag of the player whose data will be displayed.
`PLAYER_AVATAR` is a link to their Steam avatar.

- By creating a virtual environment first, or otherwise, install the required python libraries by running `pip install requirements.txt`.
- Run `streamlit run dashboard.py`.

## Files Explained
- `database.py`: Collects data from the database.
- `charts.py`: Creates the charts and the data to be displayed using `altair` and `pandas`.
- `dashboard.py`: Creates a `streamlit` dashboard and puts all of the information there.


