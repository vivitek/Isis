#!/usr/bin/env python3

from flask import Flask

app=Flask(__name__)

@app.route('/<url>')
def isis(url):
    return url

if __name__ == '__main__':
    app.run()
