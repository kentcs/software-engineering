Feature: Verify that inventors are reported on Wikipedia

Scenario: Edison invented the light bulb
  Given we navigate to Wikipedia
   When we search for "light bulb"
   Then we see that Edison is mentioned

Scenario: Wright (brothers) invented the airplane
  Given we navigate to Wikipedia
   When we search for "airplane"
   Then we see that Wright is mentioned

Scenario Outline: Inventors credited with inventions
  Given we navigate to Wikipedia
    When we search for "<invention>"
    Then we see that <inventor> is mentioned
    
    Examples:  Aviation
    | inventor | invention | 
    | Sikorsky | helicopter |
    | Wright | airplane |

    Examples: Appliances
    | inventor | invention | 
    | Edison | light bulb | 
    | Bell | telephone | 
