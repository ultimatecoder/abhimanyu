#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os

import flask
from flask_sqlalchemy import SQLAlchemy
import flask_migrate


app = flask.Flask(__name__)

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
    "SQLALCHEMY_DATABASE_URI", f"sqlite:///{BASE_DIR}/temp.db"
)

app.secret_key = os.environ.get("SECRET_KEY", "123456")

db = SQLAlchemy(app)

migrate = flask_migrate.Migrate(app, db)
