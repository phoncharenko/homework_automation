# coding: utf8

from selenium import webdriver

dr = webdriver.Chrome(executable_path="/home/paul/workspace/homework_automation/chromedriver")
dr.get("https://novaposhta.ua/")
dr.implicitly_wait(5)

dropdown = dr.find_element_by_xpath('//a[contains(text(),"Про компанію")]')
dropdown.click()
dropdown.find_element_by_xpath('//a[contains(text(),"Школа бізнесу")]').click()