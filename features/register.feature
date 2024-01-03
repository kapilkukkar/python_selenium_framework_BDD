Feature: register account functionality


  Scenario: Register with mandatory field
    Given I navigate to the register page
    When I enter details into mandatory fields
    And I click on the Continue Button
    Then the account should be created


  Scenario: Register with duplicate email address
    Given I navigate to the register page
    When I enter details into all fields except the email field
    And I enter an existing email into the email field
    And I click on the Continue Button
    Then a proper warning message should be displayed

  @register
  Scenario: Register without providing any details
    Given I navigate to the register page
    When I enter nothing into fields
    And I click on the Continue Button
    Then proper warning messages for every field should be displayed
