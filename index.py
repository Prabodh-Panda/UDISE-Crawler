import time
from tkinter.simpledialog import askstring
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import ocr

service = Service(executable_path="./lib/chromedriver.exe")
driver = webdriver.Chrome(service=service)

root_url = "https://src.udiseplus.gov.in/"
driver.get(root_url)

pincode_radio = driver.find_element(By.ID, "byPinCode")
pincode_radio.click()

pincode = askstring("Pincode", "Please enter the pincode")
search_field = driver.find_element(By.ID, "search")
search_field.send_keys(pincode)

captchaImg = driver.find_element(By.ID, "captchaId")
captchaImg.screenshot("captcha.png")

captcha = ocr.getCaptcha('captcha.png')
# captcha = askstring("Captcha", "Please enter the captcha")
captcha_field = driver.find_element(By.NAME, "captcha")
captcha_field.send_keys(captcha)

submit_btn = driver.find_element(By.ID, "homeSearchBtn")
submit_btn.click()

entries = Select(driver.find_element(By.NAME, "example_length"))
entries.select_by_value("1000")

links = driver.find_elements(By.CLASS_NAME, "clickLink")
for link in links:
    link.click()
    windows = driver.window_handles
    driver.switch_to.window(windows[1])

    driver.save_screenshot("test.png")
    elem = driver.find_element(By.ID)
    # for header in headers:
    #     print(header.text)
    #     time.sleep(2)

    time.sleep(5)

    driver.close()
    driver.switch_to.window(windows[0])

time.sleep(5)
driver.quit()