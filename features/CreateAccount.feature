# Created by zeno
Feature: Create Account Test
  This test tests whether creating an account works properly.

  Scenario: try to create account with invalid email
    Given User is on create account site
    And all fields are filled
    When create account button gets pushed
    Then process will fail
    And inform the user that one must use a valid email

  Scenario: try to create account with existing email
    Given User is on create account site
    And all fields are filled
    And email allready exists in database
    When create account button gets pushed
    Then process will fail
    And inform the user that every email is only to be registered once

  Scenario: try to create account without password
    Given User is on create account site
    And all fields except password are filled
    When create account button gets pushed
    Then process will fail
    And inform the user that one must fill out all fields

  Scenario: try to create account without name
    Given User is on create account site
    And all fields except name are filled
    When create account button gets pushed
    Then process will fail
    And inform the user that one must fill out all fields

  Scenario: try to create account without surname
    Given User is on create account site
    And all fields except surname are filled
    When create account button gets pushed
    Then process will fail
    And inform the user that one must fill out all fields

  Scenario: try to create account without email
    Given User is on create account site
    And all fields except e-mail are filled
    When create account button gets pushed
    Then process will fail
    And inform the user that one must fill out all fields

  Scenario: try to create account with invalid password second time
    Given User is on create account site
    And all fields are filled
    And passwords in both fields are not the same
    When create account button gets pushed
    Then process will fail
    And inform the user that one password is not equal to the other