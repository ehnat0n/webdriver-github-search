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

  Scenario: Navigate to
    When Navigate to project homepage
    Then Wait for 5 seconds

  Scenario: Search for user
    When Navigate to project homepage
    And I search for ehnat0n using search button
    Then Wait for 5 seconds