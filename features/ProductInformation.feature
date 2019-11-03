# Created by zeno
Feature: Get Product Information Test
  # Enter feature description here

  Scenario: no picture available for clicked product
    Given product overview is open
    When clicked on product
    Then Produt page will be shown
    And message says there are no pictures available

  Scenario: size information missing
    Given product overview is open
    When clicked on product
    Then Produt page will be shown
    And message says a size information is missing
    And one should contact the seller

  Scenario: database entry for product is not available
    Given product overview is open
    When clicked on product
    Then user will be informed that product is not available