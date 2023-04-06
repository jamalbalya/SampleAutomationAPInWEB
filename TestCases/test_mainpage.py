from elements.elements import *
import time

class BasePage(object):
    def __init__(self, driver):
        self.driver = driver
        driver.implicitly_wait(15)

class MainPage(BasePage):
    def main_webpage(self):
        print("Running main_webpage function...")
        time.sleep(3)
        element_cari_advokat = self.driver.find_element(*MainPageLocators.MENU_CARI_ADVOKAT)
        element_cari_advokat.click()
        time.sleep(3)

        from_advokat_to_main_page = self.driver.find_element(*MainPageLocators.MAIN_LOGO_ADVOKAT)
        from_advokat_to_main_page.click()
        time.sleep(3)

        element_menu_blog = self.driver.find_element(*MainPageLocators.MENU_BLOG)
        element_menu_blog.click()
        time.sleep(3)

        from_blog_back_to_main_page = self.driver.find_element(*MainPageLocators.MAIN_LOGO_BLOG)
        from_blog_back_to_main_page.click()
        time.sleep(3)

        element_menu_faq = self.driver.find_element(*MainPageLocators.MENU_FAQ)
        element_menu_faq.click()
        time.sleep(3)

        from_faq_back_to_main_page = self.driver.find_element(*MainPageLocators.MAIN_LOGO_FAQ)
        from_faq_back_to_main_page.click()
        time.sleep(3)

