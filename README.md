# easyscoreboard
An easy scoreboard.


## How to run PostgreSQL in Docker?

`Start PostgreSQL using:`

```bash
$docker run --name containerName -e POSTGRES_PASSWORD=somepassword -p 5432:5432 -d <image>
```

`Authenticate to start using as postgres user`

```bash
$docker exec -it <containerId/containerName> psql -U <userName> <databaseName>

$docker exec -it <containerId> psql -U <user> appName
```

`CREATE DATABASE and GRANT PRIVILEGES on docker interactive mode`

```bash

$docker exec -it <containerName> psql -U <imageName> -c "CREATE DATABASE databaseName ENCODING  'endocingType' TEMPLATE template0 LC_COLLATE <lcCollateType> LC_CTYPE 'lcCType';"

$docker exec -t <containerName> psql -U <user> -c "GRANT ALL PRIVILEGES ON DATABASE <dbName> TO <user>;"
```


