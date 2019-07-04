#! /usr/bin/env python

import behave

import utils


@given(u'below user already exists')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given below user already exists')


@given(u'I am logged in as "ajay.sharma@gmail.com"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given I am logged in as "ajay.sharma@gmail.com"')


@behave.when(u'I open a Signup page')
def step_impl(context):
    context.browser.get("http://localhost:5000/signup")


@behave.when(u'I type "{first_name}" as my first name')
def step_impl(context, first_name):
    first_name_input = context.browser.find_element_by_id("firstNameInput")
    first_name_input.send_keys(first_name)

@when(u'I type "{last_name}" as my last name')
def step_impl(context, last_name):
    last_name_input = context.browser.find_element_by_id("lastNameInput")
    last_name_input.send_keys(last_name)


@when(u'I type "{email_address}" as my email address')
def step_impl(context, email_address):
    email_address_input = context.browser.find_element_by_id(
        "emailaddressInput"
    )
    email_address_input.send_keys(email_address)


@when(u'I type "{password}" as my password')
def step_impl(context, password):
    password_input = context.browser.find_element_by_id("passwordInput")
    password_input.send_keys(password)

@when(u'I type "{retype_password}" as my re-type password')
def step_impl(context, retype_password):
    retype_password_input = context.browser.find_element_by_id(
        "retypePasswordInput"
    )
    retype_password_input.send_keys(retype_password)

@when(u'I press a signup button')
def step_impl(context):
    signup_button = context.browser.find_element_by_id("signupButton")
    signup_button.click()

@then(u'I should get an error message that "{warning_message}"')
def step_impl(context, warning_message):
    warning_message_element = context.browser.find_element_by_id("warning")
    utils.custom_assert(warning_message_element.text, warning_message)


@then(u'I should be logged in as "{email_address}"')
def step_impl(context, email_address):
    raise NotImplementedError(u'STEP: Then email address should be "raj.debnath@gmail.com"')


@then(u'I should be at home page')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I should be at home page')


@then(u'first name should be "{first_name}"')
def step_impl(context, first_name):
    first_name_input = context.browser.find_element_by_id("firstNameInput")
    first_name_input_value = first_name_input.get_attribute("value")
    utils.custom_assert(first_name_input_value, first_name)


@then(u'first name should be blank')
def step_impl(context):
    first_name_input = context.browser.find_element_by_id("firstNameInput")
    first_name_input_value = first_name_input.get_attribute("value")
    utils.custom_assert(first_name_input_value, "")


@then(u'last name should be "{last_name}"')
def step_impl(context, last_name):
    last_name_input = context.browser.find_element_by_id("lastNameInput")
    last_name_input_value = last_name_input.get_attribute("value")
    utils.custom_assert(last_name_input_value, last_name)


@then(u'last name should be blank')
def step_impl(context):
    last_name_input = context.browser.find_element_by_id("lastNameInput")
    last_name_input_value = last_name_input.get_attribute("value")
    utils.custom_assert(last_name_input_value, "")


@then(u'email address should be "{email_address}"')
def step_impl(context, email_address):
    email_address_input = context.browser.find_element_by_id(
        "emailaddressInput"
    )
    email_address_input_value = email_address_input.get_attribute("value")
    utils.custom_assert(email_address_input_value, email_address)


@then(u'email address should be blank')
def step_impl(context):
    email_address_input = context.browser.find_element_by_id(
        "emailaddressInput"
    )
    email_address_input_value = email_address_input.get_attribute("value")
    utils.custom_assert(email_address_input_value, "")


@then(u'password should be blank')
def step_impl(context):
    password_input = context.browser.find_element_by_id("passwordInput")
    password_input_value = password_input.get_attribute("value")
    utils.custom_assert(password_input_value, "")


@then(u're-type password should be blank')
def step_impl(context):
    retype_password = context.browser.find_element_by_id("retypePasswordInput")
    retype_password_value = retype_password.get_attribute("value")
    utils.custom_assert(retype_password_value, "")
