Feature: The parser can recognize numbers 

  Scenario: We can parse a single digit number
    Given we have a string "2"
     When we call the parse function with that string
     Then we should get a 2

  Scenario: We can parse a multiple digit number
    Given we have a string "22"
     When we call the parse function with that string
     Then we should get a 22

  Scenario: We can parse a multiple digit number
    Given we have a string "2.2"
     When we call the parse function with that string
     Then we should get a 2.2

  Scenario: We can parse a multiple digit number
    Given we have a string "2.2345"
     When we call the parse function with that string
     Then we should get a 2.2345
