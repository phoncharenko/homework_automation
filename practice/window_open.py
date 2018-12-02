from selenium import webdriver
from selenium.webdriver.common.keys import Keys

dr = webdriver.Chrome(executable_path="/home/paul/workspace/homework_automation/chromedriver")
dr.implicitly_wait(5)
dr.get("https://google.com/")

original_window = dr.current_window_handle
new_window = dr.window_handles[-1]

print(dr.window_handles)
print(dr.current_window_handle)

ac = webdriver.ActionChains(dr)
el = dr.find_element_by_xpath('//*[@id="fsr"]/a[1]')
ac.key_down(Keys.CONTROL).click(el).perform()

print(dr.current_window_handle)

dr.switch_to_window(new_window)
print(dr.get_window_size())