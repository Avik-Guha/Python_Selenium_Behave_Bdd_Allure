Feature: Verify Registration Page

  @Sanity
  Scenario: Enter Correct Username
    Given Launch application page
    When User enters "username"

  @Regression
  Scenario: Enter Incorrect Username
    Given Launch application page
    When User enters "username"