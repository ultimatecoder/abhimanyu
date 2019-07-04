#! /usr/bin/env python

import behave
from selenium import webdriver


@behave.fixture
def selenium_browser(context):
    context.browser = webdriver.Firefox()
    yield context.browser
    context.browser.quit()


def before_all(context):
    behave.use_fixture(selenium_browser, context)
