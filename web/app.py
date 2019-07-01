#! /usr/bin/env python

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/signup', methods=["GET", "POST"])
def signup():
    return render_template('signup.html')
