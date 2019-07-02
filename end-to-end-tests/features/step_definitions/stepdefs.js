const assert = require('assert');
const { Given, When, Then } = require('cucumber');
const { driver } = require('../selenium_instance');

//module.exports = function() {
//  this.When('I am not logged in', function () {
//   // Write code here that turns the phrase above into concrete actions
//   return 'pending';
//  });
//
//  this.When('I open a Signup page', function () {
//    return this.driver.get('https://google.com');
//  });

When('I am not logged in', function () {
 // Write code here that turns the phrase above into concrete actions
  return 'pending';
});

When('I open a Signup page', function () {
  return driver.get('https://google.com');
});

  //When('I type {string} as my first name', function (string) {
  // // Write code here that turns the phrase above into concrete actions
  // return 'pending';
  //});

  //When('I type {string} as my last name', function (string) {
  // // Write code here that turns the phrase above into concrete actions
  // return 'pending';
  //});

  //When('I type {string} as my email address', function (string) {
  // // Write code here that turns the phrase above into concrete actions
  // return 'pending';
  //});

  //When('I type {string} as my password', function (string) {
  // // Write code here that turns the phrase above into concrete actions
  // return 'pending';
  //});

  //When('I type {string} as my re-type password', function (string) {
  // // Write code here that turns the phrase above into concrete actions
  // return 'pending';
  //});

  //When('I press a Signup button', function () {
  // // Write code here that turns the phrase above into concrete actions
  // return 'pending';
  //});

  //Then('I should get {string} message', function (string) {
  // // Write code here that turns the phrase above into concrete actions
  // return 'pending';
  //});

  //Then('I should get an error message that {string}', function (string) {
  // // Write code here that turns the phrase above into concrete actions
  // return 'pending';
  //});

  //Given('below user already exists', function (dataTable) {
  // // Write code here that turns the phrase above into concrete actions
  // return 'pending';
  //});

  //Given('I am logged in applicant', function () {
  // // Write code here that turns the phrase above into concrete actions
  // return 'pending';
//});
//}
