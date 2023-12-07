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

  Scenario: The user’s component populates Full Name, Twitter, Bio, Company Name, Location, and Blog
    When I set username as nadvolod and save it to user_name
    And I get user info from GitHub API and save it to feature.user_data
      | context.user_name |
    And Navigate to project homepage
    And I search for user using search button
      | context.user_name |

  Scenario Outline:
    Then Displayed <data> matches API response
      | context.feature.user_data |

    Examples:
      | data         |
      | Full Name    |
      | Twitter      |
      | Bio          |
      | Company Name |
      | Location     |
      | Blog         |

  Scenario: For not existing data blank fields should be displayed, location - "earth"
    When I set username as ehnat0n and save it to user_name
    And I update test user with empty_data
      | context.user_name |
    And I get user info from GitHub API and save it to feature.user_data
      | context.user_name |
    And Navigate to project homepage
    And I search for user using search button
      | context.user_name |
    And Wait for 1 seconds

  Scenario Outline:
    Then Displayed <data> matches API response
      | context.feature.user_data |

    Examples:
      | data         |
      | Full Name    |
      | Twitter      |
      | Bio          |
      | Company Name |
      | Location     |
      | Blog         |

  Scenario: All data should be updated (page refresh) once changes applied on GitHub app
    When I set username as ehnat0n and save it to user_name
    And I update test user with full_data
      | context.user_name |
    And I get user info from GitHub API and save it to feature.user_data
      | context.user_name |
    And Navigate to project homepage
    #And Refresh the page
    And I search for user using search button
      | context.user_name |
    And Wait for 1 seconds

  Scenario Outline:
    Then Displayed <data> matches API response
      | context.feature.user_data |

    Examples:
      | data         |
      | Full Name    |
      | Twitter      |
      | Bio          |
      | Company Name |
      | Location     |
      | Blog         |
