#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sqlalchemy
import flask
from flask_sqlalchemy import SQLAlchemy

import app


db = SQLAlchemy(app.app)


class User(db.Model):
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    email_address = db.Column(
        db.String(120), unique=True, primary_key=True, nullable=False
    )
    password = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return f"<User: {self.email_address}>"

    def login(self):
        flask.session["email_address"] = self.email_address
        return True
