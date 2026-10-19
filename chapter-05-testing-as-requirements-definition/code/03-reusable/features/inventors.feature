Feature: Inventors on Wikipedia

  Scenario Outline: An invention's page names its inventor
    Given I have opened the Wikipedia home page
    When I search for <invention>
    Then the page text contains <inventor>

    Examples:
      | invention  | inventor |
      | Light Bulb | Edison   |
      | Helicopter | Sikorsky |
