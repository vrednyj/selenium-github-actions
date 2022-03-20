### Selenium tester

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time  
from Selenium.webdriver.common.keys import Keys  

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
    build_selection = driver.find_element("name",'q')
    build_selection.send_keys("What the time is now?")
except Exception as e:
    total_errors +=1
    print(e)
time.sleep(3)

try:
    build_selection = driver.find_element("name",'"btnK"')
    build_selection.send_keys(Keys.ENTER)
except Exception as e:
    total_errors +=1
    print(e)
time.sleep(3)

print("Total errors of this test: {}".format(total_errors)
driver.close() #close the web page.
