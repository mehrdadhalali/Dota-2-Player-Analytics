psql postgres -c "CREATE DATABASE dota;"
psql dota -f schema.sql
python3 seed_database.py