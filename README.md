# easyscoreboard
An easy scoreboard.


### How to run PostgreSQL in Docker?

`Start PostgreSQL using:`

```
$ docker run --name containerName -e POSTGRES_PASSWORD=somepassword -p 5432:5432 -d postgres
```

`Authenticate to start using as postgres user`

```
$ docker exec -it <containerId/containerName> psql -U <userName> <databaseName>

$ docker exec -it <containerId> psql -U postgres appName

```



