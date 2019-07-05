#! /usr/bin/env python

import os

import behave
from selenium import webdriver

from models import db


@behave.fixture
def selenium_browser(context):
    context.browser = webdriver.Firefox()
    yield context.browser
    context.browser.quit()


@behave.fixture
def db_session(context):
    context.db = db
    context.db.create_all()
    yield context.db
    context.db.drop_all()


def before_feature(context, feature):
    behave.use_fixture(selenium_browser, context)


def before_scenario(context, scenario):
    behave.use_fixture(db_session, context)
