Feature: Inventors on wikipedia get credit

  Scenario: go to wikipedia
     Given we have a browser
      When go to Wikipedia
      Then "Wikipedia" will be in the page title
       And close the browser

  Scenario: Edison gets credit for light bulbs
     Given we have a browser
      When go to Wikipedia
       And we search for "light bulb"
      Then "Edison" will be in the page content
       And close the browser

  Scenario: Sikorsky gets credit for helicopters
     Given we have a browser
      When go to Wikipedia
       And we search for "helicopter"
      Then "Sikorsky" will be in the page content
       And close the browser
