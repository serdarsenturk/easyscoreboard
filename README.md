# Easy Score Board
An easy scoreboard.

# How to set up Python development environment

```
mkdir easyscoreboard
cd easyscoreboard
python3 -m venv env
source env/bin/activate
```

`Flask Setup:`
```bash
pip3 install flask gunicorn
pip3 freeze > requirements.txt
pip3 install -r requirements.txt
```

`Start to Flask app following commands:`
```
flask run
```

## How to run PostgreSQL in Docker?

`Start PostgreSQL using:`

```bash
docker run --name mypostgresql -e POSTGRES_PASSWORD=somepassword -p 5432:5432 -d postgres:latest
```

`CREATE DATABASE and GRANT PRIVILEGES on docker interactive mode as postgres user`

```bash
docker exec -it mypostgresql psql -U postgres -c "CREATE DATABASE easyscoreboard ENCODING 'UTF8' TEMPLATE template0 LC_COLLATE 'C' LC_CTYPE 'C';"

docker exec -t mypostgresql psql -U postgres -c "GRANT ALL PRIVILEGES ON DATABASE easyscoreboard TO postgres;"
```

`Authenticate to start using as postgres user:`

```bash
docker exec -it mypostgresql psql -U postgres easyscoreboard
```

## Alembic startup configuration

`Export DB_CONNECTION_STRING URI:`

```
export DB_CONNECTION_STRING=postgresql://postgres:mysecretpassword@0.0.0.0:5432/easyscoreboard
```

## How to deploy production to Heroku

Create virtual environment:
```
python -m venv venv/
```

Activate it with `source` command:
```
source venv/bin/activate
```

Build procfile and install dependencies on app:
```
pipenv install -r requirements.txt
```

Commit last changes:
```
git commit -m "first commit"
```

Deploy app on Heroku:
```
git push heroku master
```
