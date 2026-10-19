Feature: Numbers typed into spreadsheet cells
  My spreadsheet lives or dies on reading what I type the way I mean it.
  A cell that holds a number must hold exactly that number, and a cell
  that does not hold a number must say so instead of guessing.

  Scenario Outline: A cell that holds a number
    When I type "<entry>" into a cell
    Then the cell holds the number <number>

    Examples: Whole numbers
      | entry | number |
      | 7     | 7      |
      | 0     | 0      |
      | 42    | 42     |
      | 105   | 105    |
      | 007   | 7      |

    Examples: Decimals
      | entry | number |
      | 12.5  | 12.5   |
      | 0.25  | 0.25   |
      | 10.02 | 10.02  |
      | .5    | 0.5    |
      | 5.    | 5      |

    Examples: Signs
      | entry | number |
      | -12.5 | -12.5  |
      | +7    | 7      |
      | -0.25 | -0.25  |

  Scenario Outline: A cell that does not hold a number
    When I type "<entry>" into a cell
    Then the cell is rejected as not a number

    Examples: Not numbers
      | entry |
      | abc   |
      | 12x   |
      | 1.2.3 |
      | +     |
      | -     |
      | .     |
      | --7   |
      | 1e3   |
