# Dota 2 Player Analysis
This repository analyses a Dota 2 player's performance, and provides valuable performance insights, such as win-rate, and most-played heroes, as well as the individual hero win-rate.

## Structure
- `database`: This folder creates and seeds a local database using PostgreSQL that stores the player's match data.
- `pipeline`: This folder contains a script that extracts data from the Dota 2 API and uploads it to the database.
- `dashboard`: This folder creates a `streamlit` dashboard to display some insights on the player's performance.

## Setup
To use this repository, follow the steps below:
1. Setup the database using [the instructions in the database folder](./database/README.md).
2. Fill the database with data using [the instructions in the pipeline folder](./pipeline/README.md).
3. Create and view the dashboard using [the instructions in the dashboard folder](./dashboard/README.md).