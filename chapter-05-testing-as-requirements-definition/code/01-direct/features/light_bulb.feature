Feature: Inventors on Wikipedia

  Scenario: The light bulb page mentions Edison
    Given I have opened the Wikipedia home page
    When I search for Light Bulb
    Then the page text contains Hanks
