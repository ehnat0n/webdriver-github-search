Feature: User Info
"""
Tests related to the User Info component.

Requirements:

1. The user’s component populates Full Name, Twitter, Bio, Company Name, Location, and Blog:
  - Blog link redirects to the corresponding URL
  - All data should be updated (page refresh) once changes applied on GitHub app

2. The follow button should redirect to GitHub.

3. For not existing data blank fields should be displayed:
  - Location shows 'earth' value
"""

  Scenario: The follow button should redirect to GitHub
    Given I set username as nadvolod and save it to user_name
    When Navigate to project homepage
    And I search for user using Search Button
      | context.user_name |
    Then Follow button should redirect to the user's GitHub profile
      | context.user_name |

  Scenario: Blog link redirects to the corresponding URL
    Given I set username as nadvolod and save it to user_name
    When Navigate to project homepage
    And I search for user using Search Button
      | context.user_name |
    Then Blog link should redirect to the displayed URL

  Scenario: Get user info with full data and save it on feature level
    Given I set username as nadvolod and save it to user_name
    When I get user info from GitHub API and save it to feature.user_data
      | context.user_name |
    Then I verify the response code is 200
      | context.feature.user_data |
    When Navigate to project homepage
    And I search for user using Search Button
      | context.user_name |

  Scenario Outline: The user’s component populates Full Name, Twitter, Bio, Company Name, Location, and Blog
    Then Displayed User Info <data> matches API response
      | context.feature.user_data |

    Examples:
      | data         |
      | Full Name    |
      | Twitter      |
      | Bio          |
      | Company Name |
      | Location     |
      | Blog         |

  Scenario: Get user info with empty data and save it on feature level
    Given I set username as ehnat0n and save it to user_name
    When I update test user with empty_data and save the response to response_data
      | context.user_name |
    Then I verify the response code is 200
      | context.response_data |
    Given I get user info from GitHub API and save it to feature.user_data
      | context.user_name |
    When Navigate to project homepage
    And I search for user using Search Button
      | context.user_name |

  Scenario Outline: For non existing data blank fields should be displayed, location - "earth"
    Then Displayed User Info <data> matches API response
      | context.feature.user_data |

    Examples:
      | data         |
      | Full Name    |
      | Twitter      |
      | Bio          |
      | Company Name |
      | Location     |
      | Blog         |

  Scenario: Get user info after filling all the fields and save it on feature level
    Given I set username as ehnat0n and save it to user_name
    When I update test user with full_data and save the response to response_data
      | context.user_name |
    Then I verify the response code is 200
      | context.response_data |
    And I get user info from GitHub API and save it to feature.user_data
      | context.user_name |
    And Navigate to project homepage
    And I search for user using Search Button
      | context.user_name |

  Scenario Outline: All data should be updated (page refresh) once changes applied on GitHub app
    Then Displayed User Info <data> matches API response
      | context.feature.user_data |

    Examples:
      | data         |
      | Full Name    |
      | Twitter      |
      | Bio          |
      | Company Name |
      | Location     |
      | Blog         |
