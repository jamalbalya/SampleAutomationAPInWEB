from unittest import runner
from selenium import webdriver
import unittest
from TestCases import test_mainpage


# Initialize the webdriver
driver = webdriver.Chrome()

# Run TestCases
class PythonOrg(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get("https://perqara.com/")
        cls.driver.maximize_window()

    def test_mainpage(self):
        mainPage = test_mainpage.MainPage(self.driver)
        mainPage.main_webpage()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print("Test Completed")

if __name__ == "__main__":
    unittest.main()