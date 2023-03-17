### This script was used to collect ~300 PDF files with minutes of the Israeli Northern District Planning Committee. 
### It currently collects the minutes, but could be alternated to collect the summarized protocol or the initial agenda.  
### Requires installation of selenium and selenium_stealth. 

import time
from datetime import date, datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium_stealth import stealth
from selenium.webdriver.common.by import By

options = Options()
options.add_argument("start-maximized")

# Chrome is controlled by automated test software
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
prefs = {'profile.default_content_setting_values.automatic_downloads': 1}
options.add_experimental_option("prefs", prefs)
s = Service('C:\\Program Files (x86)\\chromedriver.exe')
driver = webdriver.Chrome(service=s, options=options)

# Selenium Stealth settings
stealth(driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
        )
today = date.today()
print("Date: ", today)
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time[:-3])

driver.get("https://mavat.iplan.gov.il/SV7/10/200")
time.sleep(5)
driver.find_element(By.XPATH, "//div[contains(text(),'פרטי ישיבות')]").click()
time.sleep(3)
pdfs = driver.find_elements(By.XPATH, "//div[@class='uk-grid uk-grid-collapse']/div[4]/div/a")

### If what you want is not the session minutes, but rather the protocol or session agenda, change the number in div[4]
for pdf in pdfs[0:300]:
    try:
        pdf.click()
        time.sleep(0.1)
    except:
        time.sleep(3)

        
driver.quit()
