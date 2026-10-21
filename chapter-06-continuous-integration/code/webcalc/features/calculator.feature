Feature: Use the calculator in a real browser
  The calculator should accept button clicks and keyboard input,
  show the result, and let me recover from an error.

  Background:
    Given I open the calculator

  Scenario Outline: Calculate with the four operators
    When I click the buttons "<buttons>"
    Then the display is "<result>"

    Examples:
      | buttons | result |
      | 2 + 3 = | 5      |
      | 3 - 8 = | -5     |
      | 6 * 7 = | 42     |
      | 7 / 2 = | 3.5    |

  Scenario: Enter decimal numbers
    When I click the buttons ". 2 5 + . 5 ="
    Then the display is "0.75"

  Scenario: Change the sign
    When I click the buttons "1 2 +/-"
    Then the display is "-12"
    When I click the buttons "+/-"
    Then the display is "12"

  Scenario: Clear the entire calculation
    When I click the buttons "9 + 4 C"
    Then the display is "0"
    When I click the buttons "2 ="
    Then the display is "2"

  Scenario: Replace only the current entry
    When I click the buttons "9 + 4 5 CE"
    Then the display is "0"
    When I click the buttons "2 ="
    Then the display is "11"

  Scenario: Recover from division by zero
    When I click the buttons "8 / 0 ="
    Then the display is "Error"
    When I click the buttons "7 + 2 ="
    Then the display is "9"

  Scenario: Evaluate each operation as it is entered
    When I click the buttons "2 + 3 *"
    Then the display is "5"
    When I click the buttons "4 ="
    Then the display is "20"

  Scenario: Enter a calculation on the keyboard
    When I type "12+3"
    And I press the "Enter" key
    Then the display is "15"
    When I press the "Escape" key
    Then the display is "0"

  Scenario: Start a new entry after a result
    When I click the buttons "2 + 3 ="
    Then the display is "5"
    When I click the buttons "7"
    Then the display is "7"
