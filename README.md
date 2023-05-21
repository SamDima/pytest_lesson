# How to start locally

1. deploy postgres locally on port 5432
2. Create env inviroment and install dependencies from requirements.txt
3. start db.sh (it will create database starwars and create table user)
4. To create starwars_test:
    1. go to alembic -> env.py -> config.set_main_option(
    "sqlalchemy.url", "postgresql://postgres:postgres@localhost:5432/starwars"
    ) change to 
     config.set_main_option(
    "sqlalchemy.url", "postgresql://postgres:postgres@localhost:5432/starwars_test"
    )
    2. go to db.sh -> CREATE DATABASE starwars -> change to CREATE DATABASE starwars_test;
    3. go to alembic -> env.py -> config.set_main_option(
    "sqlalchemy.url", "postgresql://postgres:postgres@localhost:5432/starwars_test"
    ) to config.set_main_option(
    "sqlalchemy.url", "postgresql://postgres:postgres@localhost:5432/starwars"
    )
5. run main.py


