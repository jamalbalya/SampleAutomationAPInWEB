from selenium.webdriver.common.by import By

class MainPageLocators(object):
    MAIN_LOGO_ADVOKAT = (By.XPATH, "//*[@id='__nuxt']/main/body/main/div[1]/div/div[1]/div/div[3]/div/div[1]/button[2]/img")
    MAIN_LOGO_BLOG = (By.XPATH, "/html/body/header/div[1]/div/div[1]/a/img")
    MAIN_LOGO_FAQ = (By.XPATH, "//*[@id='__nuxt']/main/body/main/div[1]/div[1]/div/div[3]/div/div[1]/button[2]/img")
    BUTTON_KONSULTASI_SEKARANG = (By.XPATH, "//*[@id='value-3']/div/div[2]/button/label")
    MENU_CARI_ADVOKAT = (By.XPATH, "//*[@id='navbar-default']/ul/li[2]/a/a")
    MENU_BLOG = (By.XPATH, "//*[@id='navbar-default']/ul/li[3]/a/a")
    MENU_FAQ = (By.XPATH, "//*[@id='navbar-default']/ul/li[4]/a/a")
