#!/bin/bash
export PGPASSWORD=postgres
PGPASSWORD=postgres
psql -U postgres -h localhost -d postgres -w <<EOF
CREATE DATABASE starwars;
\q
EOF
alembic upgrade head