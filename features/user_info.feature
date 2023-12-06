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

  Scenario Outline: Complete user data is displayed and matches API response
    When Navigate to project homepage
    And I search for nadvolod using search button
    And I get user info for nadvolod from GitHub API and save it to user_data
    Then Displayed <data> matches API response
      | context.user_data |

    Examples:
      | data         |
      | Full Name    |
      | Twitter      |
      | Bio          |
      | Company Name |
      | Location     |
      | Blog         |

  Scenario: Verify user info
    When Navigate to project homepage
    And I search for ehnat0n using search button
    And I get user info for ehnat0n from GitHub API and save it to user_data
    Then I print the response code
      | context.user_data |
    And I print user data
      | context.user_data |