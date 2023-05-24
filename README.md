# How to start locally
0. Git clone repo and make branch  with firstName_lastName (dmitriy_karasev) (after test is done commit to this branch)
1. deploy postgres locally on port 5432
2. Create env inviroment and install dependencies from requirements.txt (pip install -r requirement.txt)
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
6. create test for update_user which need to:
    0. create test_update.py inside test_api dir
    2. Create new user (assert id is not null)
    1. Update Created user by using update_user route and assert new_name to the name you given while created 


