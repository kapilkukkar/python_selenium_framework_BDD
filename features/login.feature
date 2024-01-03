Feature: login functionality

  Background:
    Given I naviagte to Login Page

  @login
  Scenario Outline: login with valid credentials
    When I enter valid email as "<email>" and valid password as "<password>" into fields
    And I click on Login Button
    Then I login into the page
    Examples:
      | email           | password  |
      | abc@hotmail.com | 123456789 |
      | xyz@hotmail.com | 987654321 |


  @login
  Scenario: login with invalid email and valid password
    When I enter invalid email and valid password into fields
    And I click on Login Button
    Then I should get proper warning massage

  @login
  Scenario: login with valid email and invalid password
    When I enter valid email and invalid password into fields
    And I click on Login Button
    Then I should get proper warning massage

  @login
  Scenario: login with invalid credentials
    When I enter invalid email and invalid password into fields
    And I click on Login Button
    Then I should get proper warning massage

  @login
  Scenario: login without entering credentials
    When I leave empty email password fields
    And I click on Login Button
    Then I should get proper warning massage