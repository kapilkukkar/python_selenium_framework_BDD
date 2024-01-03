Feature: register account functionality

  Background:
    Given I naviagte to Login Page

  Scenario: Register with mandatory field
    When I enter details into mandatory fields
    And I click on the Continue Button
    Then the account should be created


  Scenario: Register with duplicate email address
    When I enter details into all fields except the email field
    And I enter an existing email into the email field
    And I click on the Continue Button
    Then a proper warning message should be displayed

  @register
  Scenario: Register without providing any details
    When I enter nothing into fields
    And I click on the Continue Button
    Then proper warning messages for every field should be displayed
