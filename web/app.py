#! /usr/bin/env python

import os

import flask
import sqlalchemy

from validators import form


app = flask.Flask(__name__)

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
    "SQLALCHEMY_DATABASE_URI", f"sqlite:///{BASE_DIR}/temp.db"
)

app.secret_key = os.environ.get("SECRET_KEY", "123456")


import models


@app.route('/signup', methods=["GET", "POST"])
def signup():
    if flask.request.method == "POST":
        form_fields = (
            "First name",
            "Last name",
            "Email address",
            "Password",
            "Retype password",
        )
        for name in form_fields:
            try:
                if form.is_blank(flask.request.form[name]):
                    warning_message = f"{name} is required"
                    return flask.render_template(
                        "signup.html",
                        warning_message=warning_message,
                        request=flask.request
                    ), 400
            except KeyError:
                warning_message = f"{name} is blank"
                return flask.render_template(
                    "signup.html",
                    warning_message=warning_message,
                    request=flask.request
                ), 400
        if not (
            flask.request.form["Password"] == flask.request.form["Retype password"]
        ):
            warning_message = "Password and Retype password should be same."
            return flask.render_template(
                "signup.html",
                warning_message=warning_message,
                request=flask.request
            ), 400
        try:
            new_user = models.User(
                first_name=flask.request.form["First name"],
                last_name=flask.request.form["Last name"],
                email_address=flask.request.form["Email address"],
                password=flask.request.form["Password"],
            )
            models.db.session.add(new_user)
            models.db.session.commit()
            new_user.login()
            return flask.redirect(flask.url_for("index")), 302
        except sqlalchemy.exc.IntegrityError:
            warning_message = (
                "Applicant with given email address already exists."
                " Please choose another email address."
            )
            return flask.render_template(
                "signup.html",
                warning_message=warning_message,
                request=flask.request
            ), 400
    return flask.render_template('signup.html'), 200


@app.route("/", methods=["GET"])
def index():
    return flask.render_template("index.html"), 200


@app.route("/login", methods=["GET", "POST"])
def login():
    pass
