#!/bin/bash
export PGPASSWORD=pass
PGPASSWORD=pass
psql -U postgres -h localhost -d pass -w <<EOF
CREATE DATABASE starwars_test;
\q
EOF
alembic upgrade head