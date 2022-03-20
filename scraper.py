### Selenium tester

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time  
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
#from selenium.webdriver.support.ui import 

total_errors=0

chrome_service = Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())

chrome_options = Options()
options = [
    "--headless",
    "--disable-gpu",
    "--window-size=1920,1200",
    "--ignore-certificate-errors",
    "--disable-extensions",
    "--no-sandbox",
    "--disable-dev-shm-usage"
]
for option in options:
    chrome_options.add_argument(option)

driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

driver.get('https://www.google.com/')
print(driver.title)
#driver.find_element_by_name("q").send_keys("javatpoint")  

try:
    search_field = driver.find_element("name",'q')
    search_field.send_keys("What the time is now?")
except Exception as e:
    total_errors +=1
    print(e)
time.sleep(3)

try:
    search_button = driver.find_element("name",'"btnK"')
    # search_button.send_keys(Keys.ENTER)
    search_button.click()
except Exception as e:
    total_errors +=1
    print(e)
time.sleep(3)

print("Total errors of this test: {}".format(total_errors))
driver.close() #close the web page.
