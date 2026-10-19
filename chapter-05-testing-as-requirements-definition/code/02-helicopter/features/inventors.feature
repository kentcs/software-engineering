Feature: Inventors on Wikipedia

  Scenario: The light bulb page mentions Edison
    Given I have opened the Wikipedia home page
    When I search for Light Bulb
    Then the page text contains Edison

  Scenario: The helicopter page mentions Sikorsky
    Given I have opened the Wikipedia home page
    When I search for Helicopter
    Then the page text contains Sikorsky
