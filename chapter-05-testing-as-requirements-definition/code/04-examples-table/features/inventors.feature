Feature: Inventors on Wikipedia

  Scenario Outline: An invention's page names its inventor
    Given I have opened the Wikipedia home page
    When I search for <invention>
    Then the page text contains <inventor>

    Examples: Communication
      | invention  | inventor |
      | Telephone  | Bell     |
      | Radio      | Marconi  |
      | Telegraphy | Morse    |

    Examples: Recording and light
      | invention  | inventor |
      | Phonograph | Edison   |
      | Light Bulb | Edison   |

    Examples: Flight
      | invention  | inventor |
      | Helicopter | Sikorsky |
      | Airplane   | Wright   |

    Examples: Industry
      | invention      | inventor  |
      | Printing Press | Gutenberg |
      | Steam Engine   | Watt      |
      | Dynamite       | Nobel     |
