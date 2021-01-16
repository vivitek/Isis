#!/usr/bin/env python3

from flask import Flask
import psycopg2
import smtplib
import ssl
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
app = Flask(__name__)
try:
    conn = psycopg2.connect("host={} dbname={} password={} user={}".format(os.getenv(
        "POSTGRES_URL", "localhost"), os.getenv("POSTGRES_DB"), os.getenv("POSTGRES_PWD"), os.getenv("POSTGRES_USER")))
except psycopg2.Error as err:
    print("[-] Error psql: {}".format(err.pgerror))
    quit(1)
conn.autocommit = True
cur = conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS site(url CHAR(200) NOT NULL,category CHAR(200) NOT NULL,id INT PRIMARY KEY NOT NULL)")

cur.execute("COPY site(url, category) FROM '/app/sites.csv' DELIMITER ',' CSV HEADER;")

@app.route('/')
def hello():
    return "Hello, this is not a website"


@app.route('/<url>')
def isis(url):
    postgreSQL_select_Query = "SELECT category, url FROM site WHERE url = %s"
    cur.execute(postgreSQL_select_Query, (url,))
    result = cur.fetchall()
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
    smtp_address = "{}".format(os.getenv("STMP_ADDRESS"))
    smtp_port = 465

    email_address = "{}".format(os.getenv("EMAIL_ADDRESS"))
    email_password = "{}".format(os.getenv("EMAIL_PASSWORD"))

    email_receiver = "{}".format(os.getenv("EMAIL_RECEIVER"))

    message = MIMEMultipart("alternative")
    message["Subject"] = "[Xana] Category change"
    message["From"] = "{}".format(os.getenv("EMAIL_ADDRESS"))
    message["To"] = "{}".format(os.getenv("EMAIL_RECEIVER"))

    text = '''
        Bonjour,

        Un nouvelle utilisateur a proposer une modification/nouvelle catégorie pour un site:
        {} : {}
        Vous pouvez l'ajouter a la database de xana.

        Bonne journée a vous,
        la joyeuse team de ViVi
    '''.format(url, category)

    texte_mine = MIMEText(text, 'plain')

    message.attach(texte_mine)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_address, smtp_port, context=context) as server:
        server.login(email_address, email_password)
        server.sendmail(email_address, email_receiver, message.as_string())
    return url


if __name__ == '__main__':
    app.run()
