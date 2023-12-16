#!/bin/bash

# Check if sqlite3 is installed
if ! command -v sqlite3 &> /dev/null
then
    echo "Error: sqlite3 is not installed. Please install it before running this script."
    exit 1
fi

# Check if python3 is installed
if ! command -v python3 &> /dev/null
then
    echo "Error: python3 is not installed. Please install it before running this script."
    exit 1
fi

# Check if Flask is installed
if ! python3 -m flask --version &> /dev/null
then
    echo "Error: Flask is not installed. Please install it before running this script."
    exit 1
fi

# Backup SQLite database
sqlite3 instance/volumes/sqlite.db ".backup instance/volumes/sqlite-backup-1.db"

# Set environment variables
export FLASK_APP=main
export PYTHONPATH=.:$PYTHONPATH

# Check arguments and perform migrations
if [ "$1" == "" ]; then
    python3 -m flask db migrate
elif [ "$1" != "init" ]; then
    echo 'Not a valid argument:
    Run "./migrate.sh init" the first time to build using an existing migration script
    Run "./migrate.sh" other times when the DB schema is changed'
    exit 127
fi

# Perform database upgrade
python3 -m flask db upgrade

# Run a custom command to generate data (replace 'generate_data' with your actual command)
# ... (existing script logic)

# Perform database upgrade
python3 -m flask db upgrade

# Run a custom command to generate data
python3 -m flask custom generate_data
