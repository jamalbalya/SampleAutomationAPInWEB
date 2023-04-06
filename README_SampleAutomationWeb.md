# SampleAutomationAPInWEB

Python files in the project:

    elements.py: This file contains the definition of the web elements that are used in the main page test. It uses the By class from the Selenium WebDriver to locate the elements using XPATH.

    test_mainpage.py: This file contains the definition of the MainPage class which inherits from the BasePage class. It contains the main_webpage() function which is responsible for running the main page test. This function uses the web elements defined in the elements.py file to interact with the main page of the website.

    main.py: This file is the main entry point of the application. It uses the unittest module to define the test cases and run them. It imports the MainPage class from the test_mainpage.py file to run the main page test case. The setUpClass() and tearDownClass() methods are used to set up and tear down the webdriver instance respectively. The test_mainpage() method is the actual test case that calls the main_webpage() function of the MainPage class.
