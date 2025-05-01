Feature: Login Functionality

  Background: common step
    Given User navigated to app home page
    And User click on My Account > Login menu

  @login
  Scenario: Login with valid credential
    When User enters valid email address say "demoqa03@gmail.com" as username
    And  User enters valid password say "demoqa123" as password
    And  click on login button
    Then User should get logged in successfully

  @login @DDT
  Scenario Outline: Login with set of invalid credentials
    When User enters invalid email address "<email>" as username
    And  User enters invalid password "<password>" as password
    And  click on login button
    Then Proper warning message should be displayed
    Examples:
      | email                 | password  |
      | demoqauser5@gmail.com | admin123  |
      | demoqauser6@gmail.com | demoqa123 |
      | demoqauser7@gmail.com | admin@123 |