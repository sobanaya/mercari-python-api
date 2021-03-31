from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options

options = Options()
profile_path = 'C:/Users/poker/AppData/Local/Google/Chrome/User Data/Default'
options.add_argument('--user-data-dir=' + profile_path)

# options.add_argument('--headless')
driver = webdriver.Chrome('C:\googledriver\chromedriver',options=options)
driver.get('https://www.mercari.com/jp/items/m44258550006/')
 
# search_bar = driver.find_element_by_name("q")
# search_bar.send_keys("python")
# search_bar.submit()
 
# for elem_h3 in driver.find_elements_by_xpath('//a/h3'):
#     elem_a = elem_h3.find_element_by_xpath('..')  
#     print(elem_h3.text)
#     print(elem_a.get_attribute('href'))