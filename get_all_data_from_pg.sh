#!/bin/bash

DB_USER="natalie.mo"
DB_PWD="wFVkbT-fva@JW}Ne/B?%WL:$"
DB_SERVER="pg-paris.unleash.so"
DB_NAME="test"
PG_URL="postgresql://$DB_USER:$DB_PWD@$DB_SERVER/$DB_NAME"

psql $PG_URL -c "select * from users"
