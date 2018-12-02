import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome(executable_path="/home/paul/workspace/homework_automation/chromedriver")
driver.implicitly_wait(5)
driver.maximize_window()

driver.get("https://demo.oxwall.com/")
admin_login = driver.find_element_by_id("loginAsAdmin")
admin_login.click()
name_login = driver.find_element_by_name("identity")
name_login.click()
name_login.clear()
name_login.click()
name_login.send_keys("demo")
password_field = driver.find_element_by_name("password")
password_field.click()
password_field.clear()
password_field.click()
password_field.send_keys("demo")

sign_in_button = driver.find_element_by_name("submit")
sign_in_button.click()
newsfeed = driver.find_element_by_name("status")
newsfeed.click()
newsfeed.clear()
newsfeed.click()

test_text = "Shit happens!!!:("
expected_text = test_text[:-2]

newsfeed.send_keys(test_text)
send_button = driver.find_element_by_name("save")
send_button.click()

time.sleep(2)

text_element = driver.find_elements_by_class_name("ow_newsfeed_content")

print(text_element[0].text)


assert text_element[0].text == expected_text



#Code below does not work!!!
hover_over_button = driver.find_elements_by_class_name("ow_console_more")


builder = ActionChains(driver)

builder.move_to_element(hover_over_button).click(hover_over_button).perform()