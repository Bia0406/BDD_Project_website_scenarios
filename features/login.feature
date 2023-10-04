Feature: Test the functionality of the login page,the connect button
  # Scenariu 1: email neinregistrat + o parola oarecare
  # Scenariu 2: fara email + o parola oarecare
  # Scenariu 3: email neinregistrat + fara parola
  # Scenariu 4: email cu format invalid + o parola oarecare
  # Scenariu 5: email inregistrat + o parola oarecare
  # Scenariu 6: email neinregistrat + o parola valida
  # Scenariu 7: email inregistrat + o parola valida

  @login_page
  # Scenariu 1
  Scenario: Check that "Eroare: Date incorecte." error message is displayed when user tries to login with unregistered email and any password
    Given I am on the login page
    When I insert "unregistered@yahoo.com" email
    And I insert any password
    And I click the connect button
    And I click the cookies button
    Then Error is displayed

  @login_page
  # Scenariu 2
  Scenario: Check that "Eroare: Date incorecte." error message is displayed when user tries to login without providing a email address and any password
    Given I am on the login page
    When I insert any password
    And I click the connect button
    Then Error is displayed

  @login_page
  # Scenariu 3
  Scenario: Check that "Eroare: Date incorecte." error message is displayed when user tries to login without providing a password, only with unregistered email
    Given I am on the login page
    When I insert "unregistered@yahoo.com" email
    And I click the connect button
    Then Error is displayed

  @login_page
  # Scenariu 4
  Scenario: Check that "Eroare: Date incorecte." error message is displayed when user tries to login with invalid format email and any password
    Given I am on the login page
    When I insert "invalid" email
    And I insert any password
    And I click the connect button
    Then Error is displayed

  @login_page
  # Scenariu 5
  Scenario: Check that "Eroare: Date incorecte." error message is displayed when user tries to login with valid email address and any password
    Given I am on the login page
    When I insert "bia83192@gmail.com" email
    And I insert any password
    And I click the connect button
    Then Error is displayed

  @login_page
  # Scenariu 6
  Scenario: Check that "Eroare: Date incorecte." error message is displayed when user tries to login with unregistered email address and valid password
    Given I am on the login page
    When I insert "unregistered@yahoo.com" email
    And I insert valid password
    And I click the connect button
    Then Error is displayed

  @login_page
  # Scenariu 7
  Scenario: Check that main page is displayed when user login with registered email address and valid password
    Given I am on the login page
    When I insert "bia83192@gmail.com" email
    And I insert valid password
    And I click the connect button
    Then The main page is displayed
