import time
from tkinter.simpledialog import askstring
from tkinter import messagebox
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import csv
import xpaths

service = Service(executable_path="./lib/chromedriver.exe")
driver = webdriver.Chrome(service=service)

root_url = "https://src.udiseplus.gov.in/"
driver.get(root_url)

pincode_radio = driver.find_element(By.ID, "byPinCode")
pincode_radio.click()

pincode = askstring("Pincode", "Please enter the pincode")
search_field = driver.find_element(By.ID, "search")
search_field.send_keys(pincode)

captcha = askstring("Captcha", "Please enter the captcha")
captcha_field = driver.find_element(By.NAME, "captcha")
captcha_field.send_keys(captcha)

submit_btn = driver.find_element(By.ID, "homeSearchBtn")
submit_btn.click()

entries = Select(driver.find_element(By.NAME, "example_length"))
entries.select_by_value("1000")

links = driver.find_elements(By.CLASS_NAME, "clickLink")

output = []

for link in links:
    link.click()
    windows = driver.window_handles
    driver.switch_to.window(windows[1])

    try:
        data = {}

        profile_keys = xpaths.school_profile.keys()
        for key in profile_keys:
            elem = driver.find_element(By.XPATH, xpaths.school_profile[key])
            data[key] = elem.text

        driver.find_element(By.XPATH, xpaths.steps["basic"]).click()
        time.sleep(1)
        basic_keys = xpaths.basic_details.keys()
        for key in basic_keys:
            elem = driver.find_element(By.XPATH, xpaths.basic_details[key])
            data[key] = elem.text

        driver.find_element(By.XPATH, xpaths.steps["facilities"]).click()
        time.sleep(1)
        basic_keys = xpaths.facilities.keys()
        for key in basic_keys:
            elem = driver.find_element(By.XPATH, xpaths.facilities[key])
            data[key] = elem.text

        driver.find_element(By.XPATH, xpaths.steps["room"]).click()
        time.sleep(1)
        basic_keys = xpaths.room_details.keys()
        for key in basic_keys:
            elem = driver.find_element(By.XPATH, xpaths.room_details[key])
            data[key] = elem.text

        driver.find_element(By.XPATH, xpaths.steps["enrolment"]).click()
        time.sleep(1)
        basic_keys = xpaths.enrolment.keys()
        for key in basic_keys:
            elem = driver.find_element(By.XPATH, xpaths.enrolment[key])
            data[key] = elem.text
        output.append(data)

    except:
        pass

    driver.close()
    driver.switch_to.window(windows[0])


keys = output[0].keys()
with open(f'{pincode}.csv', 'w', newline='') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(output)

messagebox.showinfo("Done", f"Crawling Complete For Pincode: {pincode} \n Wrote {len(output)} lines of data")
time.sleep(1)
driver.quit()