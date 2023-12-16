Feature: Followers
"""
Tests related to the Followers component.

1. Max number of followers should be 100

Here we want to check the following number of followers:
 - 0 - display empty list
 - 1 - display the list with one element
 - 100 - display 100 followers
 - 101 - display 100 followers
 - n (2-99) - display n followers

Use GitHub search with query like "type:user followers:101".

2. Each follower has a Name and Link

Use 100+ follower user.
Verify that every entry has a name and a link that is a valid GitHub profile link.

3. All data should be updated once changes are applied to the GitHub app

Use test account to unfollow/follow another user. Order is important!
Idempotence of the DELETE operation allows us to always execute in this order regardless of \
initial following status.

It prevents false negative: test would pass with the opposite order because user is not present \
in the followers list of the default nadvolod profile.
  """

  Scenario Outline: Max number of followers should be 100
    Given I set username as <username> and save it to username
    When I get first 100 user followers from GitHub API and save it to followers
      | username |
    Then I verify the response code is 200
      | followers |
    When Navigate to project homepage
    And I search for user using Search Button
      | username |
    Then I verify followers list length matches saved data
      | followers |

    # 0 - 100 - 1 - 101 - 42
    Examples:
      | username    |
      | A054        |
      | DevTides    |
      | kkruszewska |
      | PwC-IR      |
      | gkc1000     |

  Scenario: Each follower has a Name and Link
    Given I set username as DevTides and save it to username
    When I get first 100 user followers from GitHub API and save it to followers
      | username |
    Then I verify the response code is 200
      | followers |
    When Navigate to project homepage
    And I search for user using Search Button
      | username |
    Then I verify every follower in the list has a proper GitHub username and profile link
      | followers |

  Scenario: All data should be updated once changes are applied to the GitHub app
    Given I set username as ehnat0n and save it to username
    And I set username as kamre and save it to target_username
    When I unfollow the user and save response to response
      | username | target_username |
    Then I verify the response code is 204
      | response |
    When Navigate to project homepage
    And I search for user using Search Button
      | target_username |
    Then I verify user is not listed in the Followers component
      | target_username | username |
    When I follow the user and save response to response
      | username | target_username |
    Then I verify the response code is 204
      | response |
    When Navigate to project homepage
    And I search for user using Search Button
      | target_username |
    Then I verify user is listed in the Followers component
      | username |
