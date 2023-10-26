sqlite3 instance/volumes/sqlite.db ".backup instance/volumes/sqlite-backup-1.db"
export FLASK_APP=main
export PYTHONPATH=.:$PYTHONPATH  # flask need . to find files
if [ "$1" == "" ] # don't migrate when building for the first time (migration script already exists)
then
    python3 -m flask db migrate
elif [ "$1" != "init" ]
then
    echo 'Not a valid argument:
Run "./migrate.sh init" first time to build using exising migration script
Run "./migrate.sh" other times when DB schema is changed'
    exit 127
fi
python3 -m flask db upgrade
