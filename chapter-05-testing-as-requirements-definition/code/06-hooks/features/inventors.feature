Feature: Inventors on Wikipedia

  Background:
    Given I have opened the Wikipedia home page

  Scenario Outline: An invention's page names its inventor
    When I search for <invention>
    Then the page text contains <inventor>

    Examples:
      | invention      | inventor  |
      | Light Bulb     | Edison    |
      | Helicopter     | Sikorsky  |
      | Telephone      | Bell      |
      | Airplane       | Wright    |
      | Printing Press | Gutenberg |
      | Dynamite       | Nobel     |
      | Steam Engine   | Watt      |
      | Radio          | Marconi   |
      | Phonograph     | Edison    |
      | Telegraphy     | Morse     |

  Scenario Outline: An inventor's page names their invention
    When I search for <inventor>
    Then the page text contains <invention>

    Examples:
      | inventor              | invention      |
      | Thomas Edison         | phonograph     |
      | Igor Sikorsky         | helicopter     |
      | Alexander Graham Bell | telephone      |
      | Johannes Gutenberg    | printing press |
      | Alfred Nobel          | dynamite       |
