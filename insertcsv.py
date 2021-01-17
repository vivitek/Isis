#!/usr/bin/python3

import psycopg2
import csv

from progressbar import ProgressBar

conn = psycopg2.connect("host=localhost dbname=xanadb password=xana2020 user=xana port=5432")
conn.autocommit = True
pbar = ProgressBar()
cur = conn.cursor()

with open("./sites.csv") as csv_file:
    reader = csv.reader(csv_file)
    pbar.start()
    data = list(reader)[1:]
    for row in pbar(data):
        cur.execute("INSERT INTO site(url, category) VALUES (\'{}\', \'{}\');".format(row[0], row[1]))
##cur.execute("""
  #  COPY site(url, category)
   # FROM '/app/sites.csv'
    #DELIMITER ','
    #CSV HEADER;
#""")
