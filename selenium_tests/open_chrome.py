import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome(executable_path='/home/paul/workspace/homework_automation/chromedriver')
driver.implicitly_wait(2) # устанавливает поиск всех элементов до 2-х секунд, если быстрее, идет дальше
driver.get('https://www.google.com/')
time.sleep(2) # используем для дебаггинга
search_box = driver.find_element_by_name('q')
search_box.send_keys('itc')
search_box.submit()
time.sleep(1)
search_box = driver.find_elements_by_partial_link_text("Новости")
time.sleep(1)
print(len(search_box))
search_box = driver.find_element_by_xpath('//*[@id="hdtb-msb-vis"]/div[2]/a')
print(search_box.text)
print(search_box.size) # {'height': 15, 'width': 66}
print(search_box.location) # {'y': 92, 'x': 214}

def is_element_present(driver, by, locator):
    try:
        driver.find_element(by, locator)
    except NoSuchElementException:
        return False
    return True

# or
#def is_element_present(driver, by, locator):
#    if driver.find_element(by, locator):
#        return True
#    return False

driver.quit()
