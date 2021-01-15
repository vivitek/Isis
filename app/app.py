#!/usr/bin/env python3

from flask import Flask
import psycopg2
import smtplib, ssl

app = Flask(__name__)

conn = psycopg2.connect("host=localhost dbname=postgres password=Battle98* user=dythic")
conn.autocommit = True
cur = conn.cursor()

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
    while x <= max_count - 1 :
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
        server.sendmail(email_address, email_receiver, 'le contenu de l\'e-mail')
    return url

if __name__ == '__main__':
    app.run()
