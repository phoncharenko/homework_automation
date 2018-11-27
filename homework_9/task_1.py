# coding: utf8

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="/home/paul/workspace/homework_automation/chromedriver")
driver.get("https://novaposhta.ua/")
driver.implicitly_wait(5)

wait = WebDriverWait(driver, 10)
element = wait.until(
    EC.element_to_be_clickable(By.XPATH, '//*[@id="top_menu"]/li[1]/ul/li[7]/a')
)


#menu = driver.find_element_by_xpath('//a[contains(text(),"Про компанію")]')
#submemu = menu.find_element_by_xpath('//*[@id="top_menu"]/li[1]/ul/li[7]/a')
action = ActionChains(element)
#action.move_to_element(menu)
action.click(element).perform()
