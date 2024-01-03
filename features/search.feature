Feature: search functionality

  Background:
    Given I naviagte to Login Page

  @search
  Scenario: search for valid product
    When i entered valid product into the search box
    And i click on search button
    Then valid product should be shown in search result

  @search
  Scenario: search for an invalid product
    When i entered the invalid product in search box
    And i click on search button
    Then proper error massage should be displayed

  @search
  Scenario: search without entering any product
    When i entered the nothing product in search box
    And i click on search button
    Then proper error massage should be displayed

