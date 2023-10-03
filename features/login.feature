Feature: Test the functionality of the login page,the connect button
  # Scenariu 1: email neinregistrat + o parola oarecare
  # Scenariu 2: fara email + o parola oarecare
  # Scenariu 3: email neinregistrat + fara parola
  # Scenariu 4: email cu format invalid + o parola oarecare

  Scenario: Check that "Eroare: Date incorecte." error message is displayed when user tries to login with unregistered email
    Given I am on the login page
    When I insert "unregistered@yahoo.com" email
    And I insert a password
    And I click the connect button
    And I click the cookies button
    Then Error is displayed

  Scenario: Check that "Eroare: Date incorecte." error message is displayed when user tries to login without providing an email address
    Given I am on the login page
    When I insert a password
    And I click the connect button
    Then Error is displayed

  Scenario: Check that "Eroare: Date incorecte." error message is displayed when user tries to login without providing a password
    Given I am on the login page
    When I insert "unregistered@yahoo.com" email
    And I click the connect button
    Then Error is displayed

  Scenario: Check that "Eroare: Date incorecte." error message is displayed when user tries to login with invalid format email
    Given I am on the login page
    When I insert "invalid" email
    And I insert a password
    And I click the connect button
    Then Error is displayed

