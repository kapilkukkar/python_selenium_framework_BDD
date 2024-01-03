Feature: search functionality

  @search
  Scenario: search for valid product
    Given i got navigated to Home Page
    When i entered valid product into the search box
    And i click on search button
    Then valid product should be shown in search result

  @search
  Scenario: search for an invalid product
    Given i got navigated to Home Page
    When i entered the invalid product in search box
    And i click on search button
    Then proper error massage should be displayed

  @search
  Scenario: search without entering any product
    Given i got navigated to Home Page
    When i entered the nothing product in search box
    And i click on search button
    Then proper error massage should be displayed

