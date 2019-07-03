#! /usr/bin/env python

from flask import Flask, request, render_template

from validators import form

app = Flask(__name__)


@app.route('/signup', methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        form_fields = (
            "First name",
            "Last name",
            "Email address",
            "Password",
            "Retype password",
        )
        for name in form_fields:
            try:
                if form.is_blank(request.form[name]):
                    warning_message = f"{name} is required"
                    return render_template(
                        "signup.html", warning_message=warning_message
                    )
            except KeyError:
                warning_message = f"{name} is blank"
                return render_template(
                    "signup.html", warning_message=warning_message
                )
        if not (request.form["Password"] == request.form["Retype password"]):
            warning_message = "Password and Retype password should be same."
            return render_template(
                "signup.html", warning_message=warning_message
            )
    return render_template('signup.html', warning_message=None)
