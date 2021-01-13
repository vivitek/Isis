#!/usr/bin/env python3

from flask import Flask
import psycopg2

app=Flask(__name__)

conn = psycopg2.connect("host=localhost dbname=postgres password=password user=postgres")
conn.autocommit = True
cur = conn.cursor()
cur.execute("""
    CREATE TABLE IF NOT EXISTS site(
    url VARCHAR,
    category VARCHAR
    )
""")

@app.route('/<url>')
def isis(url):
    postgreSQL_select_Query = "SELECT category, url FROM site WHERE url = %s"
    cur.execute(postgreSQL_select_Query, (url,))
    result = cur.fetchall()
    print(result[0])
    return result[0]

@app.route("/<url>", methods=["PATCH"])
def reportError(url, category):
    # patch db
    return {url, category}

if __name__ == '__main__':
    app.run()
