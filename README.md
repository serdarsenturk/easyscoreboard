# easyscoreboard
An easy scoreboard.


## How to run PostgreSQL in Docker?

`Start PostgreSQL using:`

```bash
docker run --name containerName -e POSTGRES_PASSWORD=somepassword -p 5432:5432 -d postgres:latest
```

`CREATE DATABASE and GRANT PRIVILEGES on docker interactive mode as postgres user`

```bash
docker exec -it <containerName> psql -U postgres -c "CREATE DATABASE somedb ENCODING 'LATIN1' TEMPLATE template0 LC_COLLATE 'C' LC_CTYPE 'C';"

docker exec -t <containerName> psql -U postgres -c "GRANT ALL PRIVILEGES ON DATABASE somedb TO postgres;"
```

`Authenticate to start using as postgres user`

```bash
docker exec -it <containerId/containerName> psql -U postgres somedb
```



