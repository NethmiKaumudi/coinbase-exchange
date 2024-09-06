#!/bin/bash

# Load environment variables
export $(grep -v '^#' .env | xargs)

# Create the database if it doesn't exist
mysql -h $DB_HOST -P $DB_PORT -u $DB_USER -p$DB_PASS -e "CREATE DATABASE IF NOT EXISTS $DB_NAME;"
