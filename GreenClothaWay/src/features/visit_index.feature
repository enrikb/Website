# Created by zeno at 08.12.19
Feature: visit /index
  i want to test whether my website is reachable at all

  Scenario: visit /index successfully
    When i visit page /index
    Then the url is /index
    And the page contains clothes

#  Scenario: visit /index without succes
#    When i visit page /index
#    Then i see 404 not found
