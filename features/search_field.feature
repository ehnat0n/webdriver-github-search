Feature: Search Field
"""
Tests related to the Search Field component.

Requirements:

1. Search can be performed by typing the profile name into the search field
and Enter/Return or clicking on the Search button.

2. Search result populates data from the GitHub account corresponding to the search field:
  - User, Followers, Following, Repos and Gists details
  - User component
  - Followers component

3. Not valid username populates an empty result.
"""

  Scenario: Search for user with the Search button
    Given I set username as ehnat0n and save it to user_name
    When Navigate to project homepage
    And I search for user using Search Button
      | context.user_name |
    Then Wait for 3 seconds

  @wip
  Scenario: Search for user with the Enter Key
    Given I set username as ehnat0n and save it to user_name
    When Navigate to project homepage
    And I search for user using Enter Key
      | context.user_name |
    Then Wait for 3 seconds