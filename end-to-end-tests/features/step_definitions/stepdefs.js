const assert = require('assert');
const { Given, When, Then } = require('cucumber');
const { By } = require('selenium-webdriver');
const { getDriver } = require('../selenium_instance');

Given('below user already exists', function (dataTable) {
 // Write code here that turns the phrase above into concrete actions
 return 'pending';
});

Given('I am logged in applicant', function () {
 // Write code here that turns the phrase above into concrete actions
  return 'pending';
});

When('I open a Signup page', function () {
  return getDriver().get('http://localhost:5000/signup');
});

When('I type {string} as my first name', function (string) {
  let element = getDriver().findElement(By.id('firstNameInput'));
  return element.sendKeys(string);
});

When('I type {string} as my last name', function (string) {
  let element = getDriver().findElement(By.id('lastNameInput'));
  return element.sendKeys(string);
});

When('I type {string} as my email address', function (string) {
  let element = getDriver().findElement(By.id('emailaddressInput'));
  return element.sendKeys(string);
});

When('I type {string} as my password', function (string) {
  let element = getDriver().findElement(By.id('passwordInput'));
  return element.sendKeys(string);
});

When('I type {string} as my re-type password', function (string) {
  let element = getDriver().findElement(By.id('passwordRetypeInput'));
  return element.sendKeys(string);
});

When('I press a signup button', function () {
  let button = getDriver().findElement(By.id('submitButton'));
  return button.click();
});

Then('I should get an error message that {string}', function (string) {
  let element = getDriver().findElement(By.id('warning'));
  return element.getText().then(function(text) {
    return assert.strictEqual(text, string);
  });
});

Then('last name should be {string}', function (string) {
  let element = getDriver().findElement(By.id('lastNameInput'));
  return element.getAttribute('value').then(function(text) {
    return assert.strictEqual(text, string);
  });
});

Then('email address should be {string}', function (string) {
  let element = getDriver().findElement(By.id('emailaddressInput'));
  return element.getAttribute('value').then(function(text) {
    return assert.strictEqual(text, string);
  });
});

Then('password should be {string}', function (string) {
  let element = getDriver().findElement(By.id('passwordInput'));
  return element.getAttribute('value').then(function(text) {
    return assert.strictEqual(text, string);
  });
});

Then('re-type password should be {string}', function (string) {
  let element = getDriver().findElement(By.id('passwordRetypeInput'));
  return element.getAttribute('value').then(function(text) {
    return assert.strictEqual(text, string);
  });
});

Then('first name should be {string}', function (string) {
  let element = getDriver().findElement(By.id('firstNameInput'));
  return element.getAttribute('value').then(function(text) {
    return assert.strictEqual(text, string);
  });
});

Then('I should be logged in as {string}', function (string) {
  return 'pending';
});

Then('I should be at home page', function () {
  return 'pending';
});
