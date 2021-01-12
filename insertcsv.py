#!/usr/bin/python3

import psycopg2

conn = psycopg2.connect("host=localhost dbname=postgres password=password user=user")
conn.autocommit = True

cur = conn.cursor()

cur.execute("""
    CREATE TABLE site(
    url VARCHAR,
    category VARCHAR
    )
""")
print("Table created successfully........")

cur.execute("""
    COPY site(url, category)
    FROM '/home/dythic/Documents/xana/sites.csv'
    DELIMITER ','
    CSV HEADER;
""")
print("Insert CSV succeddfully........")

cur.execute("""SELECT * FROM site;""")

conn.commit()

conn.close()