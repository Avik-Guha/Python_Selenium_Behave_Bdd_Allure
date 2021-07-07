Feature: Verify Registration1 Page

  @Sanity
  Scenario: Enter Correct Username
    Given Launch application page
    When User enters "username"
    And User enters "password"
    And User enters "email"