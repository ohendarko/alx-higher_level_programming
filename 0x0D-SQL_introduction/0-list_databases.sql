#!/bin/bash
--  lists all databases of MySQL server.
USER="root"
PASSWORD="root"
databases=$(mysql -u"$USER" -p"$PASSWORD" -e "SHOW DATABASES;" | grep -Ev "(Database|information_schema|performance_schema)")
