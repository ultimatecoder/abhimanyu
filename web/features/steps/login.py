#! /usr/bin/env python

from models import User

import utils


@given(u'I am logged in as "{email_address}"')
def step_impl(context, email_address):
    raise NotImplementedError(u'STEP: I am logged in as email_address')


@then(u'I should be logged in as "{email_address}"')
def step_impl(context, email_address):
    email_dropdown = context.browser.find_element_by_id("userProfileDropdown")
    utils.custom_assert(email_dropdown.text, email_address)
