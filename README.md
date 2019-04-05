## Test/example repo for SAFRS

Use `./run.sh` to run misc tasks for this repo. Just `cat run.sh` to see what's available,
then `./run.sh <task> [<args>]`.

## Set up the DB
`./run.sh db up -d`

Create a database and use the uuid extension:
Launch a psql shell - manually or with `./run.sh db_shell`.

* `CREATE DATABASE safrs;`
* `\c safrs`
* `CREATE EXTENSION "uuid-ossp";`

## Run the service
`./run.sh up`

## Run tests
`./run.sh test`