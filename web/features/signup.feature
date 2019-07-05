Feature: Applicant Signup
  This functionality will allow an applicant to create his/her account

  Scenario: Signup should not be possible for logged in users
    Given below user already exists
      | first name | last name | email address         | password |
      | Ajay       | Sharm     | ajay.sharma@gmail.com  | abcs     |
    And I am logged in as "ajay.sharma@gmail.com"
    When I open a Signup page
    Then I should get an error message that "You are already logged in"

  Scenario: An applicant should be redirected to home page on successful sign up
    When I open a Signup page
    And I type "Ajay" as my first name
    And I type "Sharma" as my last name
    And I type "ajay.sharma@gmail.com" as my email address
    And I type "1234" as my password
    And I type "1234" as my re-type password
    And I press a signup button
    Then there should be an entry with "ajay.sharma@gmail.com"
    And I should be at home page
    And I should be logged in as "ajay.sharma@gmail.com"

  Scenario: Give an error when applicant with same email address already exists
    Given below user already exists
      | first name | last name | email address         | password |
      | Raj        | Debnath   | raj.debnath@gmail.com | 1234     |
      | Ajay       | Sharm     | ajay.sharm@gmail.com  | abcs     |
    When I open a Signup page
    And I type "Raj" as my first name
    And I type "Debnath" as my last name
    And I type "raj.debnath@gmail.com" as my email address
    And I type "1234" as my password
    And I type "1234" as my re-type password
    And I press a signup button
    Then I should get an error message that "Applicant with given email address already exists. Please choose another email address."

  Scenario: Give a warning when password and re-password fields are not same
    When I open a Signup page
    And I type "Raj" as my first name
    And I type "Debnath" as my last name
    And I type "raj.debnath@gmail.com" as my email address
    And I type "1234" as my password
    And I type "1235" as my re-type password
    And I press a signup button
    Then I should get an error message that "Password and Retype password should be same."
    And first name should be "Raj"
    And last name should be "Debnath"
    And email address should be "raj.debnath@gmail.com"
    And password should be blank
    And re-type password should be blank

  Scenario: Give a warning when First name is not filled
    When I open a Signup page
    And I type "Debnath" as my last name
    And I type "raj.debnath@gmail.com" as my email address
    And I type "1234" as my password
    And I type "1234" as my re-type password
    And I press a signup button
    Then I should get an error message that "First name is required"
    And last name should be "Debnath"
    And email address should be "raj.debnath@gmail.com"
    And password should be blank
    And re-type password should be blank

  Scenario: Give a warning when email address filed is blank
    When I open a Signup page
    And I type "Raj" as my first name
    And I type "Debnath" as my last name
    And I type "1234" as my password
    And I type "1235" as my re-type password
    And I press a signup button
    Then I should get an error message that "Email address is required"
    And first name should be "Raj"
    And last name should be "Debnath"
    And password should be blank
    And re-type password should be blank

  Scenario: Give a warning when Password is blank
    When I open a Signup page
    And I type "Raj" as my first name
    And I type "Debnath" as my last name
    And I type "raj.debnath@gmail.com" as my email address
    And I type "1234" as my re-type password
    And I press a signup button
    Then I should get an error message that "Password is required"
    And first name should be "Raj"
    And last name should be "Debnath"
    And email address should be "raj.debnath@gmail.com"
    And password should be blank
    And re-type password should be blank

  Scenario: Give a warning when Retype Password is blank
    When I open a Signup page
    And I type "Raj" as my first name
    And I type "Debnath" as my last name
    And I type "raj.debnath@gmail.com" as my email address
    And I type "1234" as my password
    And I press a signup button
    Then I should get an error message that "Retype password is required"
    And first name should be "Raj"
    And last name should be "Debnath"
    And email address should be "raj.debnath@gmail.com"
    And password should be blank
    And re-type password should be blank

  Scenario: Form should be blank when launched initially
    When I open a Signup page
    Then first name should be blank
    And last name should be blank
    And email address should be blank
    And password should be blank
    And re-type password should be blank
