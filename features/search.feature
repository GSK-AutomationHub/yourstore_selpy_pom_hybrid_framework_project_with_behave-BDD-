Feature: Search functionality

  Background: common step
    Given User navigated to app home page

  @search @run
  Scenario: Search for a valid product
    When User enters valid product say "HP" into the search box field
    And click on search button
    Then Valid product should get displayed in Search results

  @search
  Scenario: Search for an invalid product
    When User enters invalid product say "Honda" into the search box field
    And click on search button
    Then Proper message should be displayed in Search results

  @search
  Scenario: Search without entering any product
    When User dont enter anything into search box field
    And click on search button
    Then Proper message should be displayed in Search results