# Created by zeno at 08.12.19
Feature: Test Register
  It is important that registration is working.

  Scenario: successful registration
    When i visit page /register
    And fill in form
    And press 'sign up'
    Then account is created in database
    And user will be on profile page