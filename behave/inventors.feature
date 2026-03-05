Feature: check inventors on invention pages

Scenario Outline:
     Given we have navigated to wikipedia
      When we search for "<invention>"
      Then the resulting page will include "<inventor>"

  Examples: Electronics
    | invention | inventor |
    | Telephone | Alexander Graham Bell |
    | Transistor | Bardeen |
    | Light Bulb | Edison |
    | Phonograph | Edison |

  Examples: Transportation
    | invention | inventor |
    | Airplane | Wright |
    | Helicopter | Sikorsky |