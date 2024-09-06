#!/bin/bash

# Load environment variables
export $(grep -v '^#' .env | xargs)

# Apply migrations
mysql -h $DB_HOST -P $DB_PORT -u $DB_USER -p$DB_PASS $DB_NAME < /scripts/sql/migrations.sql
