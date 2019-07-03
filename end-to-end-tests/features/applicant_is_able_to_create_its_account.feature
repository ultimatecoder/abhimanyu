Feature: Applicant Signup
  This functionality will allow an applicant to create his/her account

  Scenario: Signup should not be possible for logged in users
    Given I am logged in applicant
    When I open a Signup page
    Then I should get an error message that "You are already logged in"

  Scenario: Ajay tries to signup himself
    When I open a Signup page
    And I type "Ajay" as my first name
    And I type "Sharma" as my last name
    And I type "ajay.sharma@gmail.com" as my email address
    And I type "1234" as my password
    And I type "1234" as my re-type password
    And I press a Signup button
    Then I should get "Signup is successful" message

  Scenario: Give an error when applicant with same email address already exists
    Given below user already exists
      | first name | last name | email                 | password |
      | Raj        | Debnath   | raj.debnath@gmail.com | 1234     |
      | Ajay       | Sharm     | ajay.sharm@gmail.com  | abcs     |
    When I open a Signup page
    And I type "Raj" as my first name
    And I type "Debnath" as my last name
    And I type "raj.debnath@gmail.com" as my email address
    And I type "1234" as my password
    And I type "1234" as my re-type password
    And I press a Signup button
    Then I should get an error message that "Applicant with given email address already exists. Please choose another email address."

  Scenario: Give a warning when password and re-password fields are not same
    When I open a Signup page
    And I type "Raj" as my first name
    And I type "Debnath" as my last name
    And I type "raj.debnath@gmail.com" as my email address
    And I type "1234" as my password
    And I type "1235" as my re-type password
    And I press a Signup button
    Then I should get an error message that "Password and Retype password should be same."

  Scenario: Give a warning when First name is not filled
    When I open a Signup page
    And I type "Debnath" as my last name
    And I type "raj.debnath@gmail.com" as my email address
    And I type "1234" as my password
    And I type "1234" as my re-type password
    And I press a Signup button
    Then I should get an error message that "First name is required"

  Scenario: Give a warning when email address filed is blank
    When I open a Signup page
    And I type "Raj" as my first name
    And I type "Debnath" as my last name
    And I type "1234" as my password
    And I type "1235" as my re-type password
    And I press a Signup button
    Then I should get an error message that "Email address is required"

  Scenario: Give a warning when Password is blank
    When I open a Signup page
    And I type "Raj" as my first name
    And I type "Debnath" as my last name
    And I type "raj.debnath@gmail.com" as my email address
    And I type "1234" as my re-type password
    And I press a Signup button
    Then I should get an error message that "Password is required"

  Scenario: Give a warning when Password is blank
    When I open a Signup page
    And I type "Raj" as my first name
    And I type "Debnath" as my last name
    And I type "raj.debnath@gmail.com" as my email address
    And I type "1234" as my password
    And I press a Signup button
    Then I should get an error message that "Retype password is required"
