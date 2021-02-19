# Alembic useful commands

This will create an environment using the “generic” template(current project directory):
```
alembic init alembic
```

Inside alembic.ini 'sqlalchemy.url' environment option. It provides to connect to the database via SQLAlchemy.
For starting up with just a single database and the generic configuration, setting up the SQLAlchemy URL is all that’s needed:
``` 
sqlalchemy.url = driver://user:pass@localhost/dbname
```

With the environment in place we can create a new revision,Every time Alembic runs an operation against the versions/ directory, using alembic revision:
```
alembic revision -m "create <tablaName> table"
```
We can then add some directives to our script, inside 'alembic/versions' directory, suppose adding a new table <tableName>:
```
def upgrade():
    op.create_table(
        '<tableName>',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('description', sa.Unicode(200)),
    )
```

```
def downgrade():
    op.drop_table('account')
```

Running our First Migration:
```
alembic upgrade head
```

Downgrading
```
alembic upgrade base
```

Getting Information:
```
alembic current
```


