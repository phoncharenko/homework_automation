from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time


dr = webdriver.Chrome(executable_path="/home/paul/workspace/homework_automation/chromedriver")
dr.implicitly_wait(7)
dr.get("https://demo.oxwall.com/")

login = dr.find_element_by_id("loginAsAdmin")
login.click()

#popup_login = dr.find_element_by_class_name("ow_bg_color")
#print(popup_login.get_attribute(popup_login))
#dr.switch_to_frame(popup_login)

login_input = dr.find_element_by_xpath('//*[@name="identity"]')
password_input = dr.find_element_by_xpath('//*[@name="password"]')
submit_bttn = dr.find_element_by_name("submit")

login_input.click()
#login_input.send_keys("admin")
password_input.click()
#password_input.send_keys("pass")
submit_bttn.click()

header_bttn = dr.find_element_by_class_name('ow_console_item')
action = ActionChains(dr)
action.move_to_element(header_bttn).pause(2).perform()
logout_bttn = dr.find_element_by_xpath('//a[contains(text(),"Sign Out")]').click()

