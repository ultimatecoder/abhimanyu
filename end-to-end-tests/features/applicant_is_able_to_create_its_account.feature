Feature: Applicant Signup
  When I am an applicant, I should be able to create my account

  Scenario: Signup without loging required
    When I am not logged in and I am trying to reach Signup page
    Then I should be able to create my account

  Scenario: Avoid duplicate usernames
    Given Applicant with username 'xyz' present in system
    When I am trying to create an account with 'xyz' username
    Then I should get an error for username already exists
