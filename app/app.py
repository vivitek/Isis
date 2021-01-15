#!/usr/bin/env python3

from flask import Flask
import psycopg2
import smtplib
import ssl
import os
app = Flask(__name__)

conn = psycopg2.connect("host={} dbname={} password={} user={}".format(os.getenv(
    "POSTGRES_URL", "localhost"), os.getenv("POSTGRES_DB"), os.getenv("POSTGRES_PWD"), os.getenv("POSTGRES_USER")))
conn.autocommit = True
cur = conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS site(url CHAR(200) NOT NULL,category CHAR(200) NOT NULL,id INT PRIMARY KEY NOT NULL)")


@app.route('/')
def hello():
    return "Hello, this is not a website"


@app.route('/<url>')
def isis(url):
    postgreSQL_select_Query = "SELECT category, url FROM site WHERE url = %s"
    cur.execute(postgreSQL_select_Query, (url,))
    result = cur.fetchall()
    print(result[0])
    return result[0]


@app.route('/find/<category>')
def sendCategory(category):
    x = 1
    site = ""
    max_count = 0
    postgreSQL_select_Count = "SELECT COUNT(category) FROM site WHERE category = %s"
    cur.execute(postgreSQL_select_Count, (category,))
    max_count = cur.fetchall()
    max_count = int(max_count[0][0])
    postgreSQL_select_Query = "SELECT url, category FROM site WHERE category = %s"
    cur.execute(postgreSQL_select_Query, (category,))
    result = cur.fetchall()
    site = result[0][0]
    while x <= max_count - 1:
        site = site + ", " + result[x][0]
        x = x + 1
    return site


@app.route("/<url>/<category>")
def reportError(url, category):
    smtp_address = 'smtp.gmail.com'
    smtp_port = 465

    email_address = ''
    email_password = ''

    email_receiver = 'quentin.henry@epitech.eu'

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_address, smtp_port, context=context) as server:
        server.login(email_address, email_password)
        server.sendmail(email_address, email_receiver,
                        'le contenu de l\'e-mail')
    return url


if __name__ == '__main__':
    app.run()
