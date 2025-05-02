Feature: Register Account functionality

  Background: common step
    Given User navigated to app home page
    And User click on My Account > Register menu

  @register @run
  Scenario: Register to app with mandatory fields
    When User enter below details into mandatory fields
      | first_name | last_name | email                | telephone  | password  |
      | demoqa107  | demoqa107  | demoqa107@testmail.com | 1234541003 | demoqa223 |
    And User select Privacy Policy option
    And User click on Continue button
    Then User account should get created successfully

  @register
  Scenario: Register to app with all fields
    When User enter details into all fields
    And User select Privacy Policy option
    And User click on Continue button
    Then User account should get created successfully

  @register
  Scenario: Register with a duplicate email address
    When User enter details into all fields except email field
    And User enter existing accounts email into email field
    And User select Privacy Policy option
    And User click on Continue button
    Then Proper warning message about duplicate account should be displayed

  @register @warnings
  Scenario: Register without providing any details
    When User dont enter anything into the fields
    And User click on Continue button
    Then Proper warning messages for missing mandatory fields should be displayed
