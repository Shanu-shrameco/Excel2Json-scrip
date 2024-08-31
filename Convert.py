import os
import random
import time
import json
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

def convertData(pyautogui=None):
    driver = webdriver.Chrome()
    driver.get('https://codebeautify.org/excel-to-json')

    time.sleep(2)

    # press upload file
    driver.find_element(By.XPATH, '//*[@id="app"]/div[3]/div/div[1]/div[1]/div/button[2]').click()

    time.sleep(2)

    time.sleep(1)

    pyautogui.write("/home/shanu/codes/python/Excel2Json/separated_columns.xlsx")

    pyautogui.press('enter')
    time.sleep(5)


    print("clicked")




    # get the output data and save it in json file
    getData = driver.find_element(By.XPATH,'//*[@id="outputACEEditor"]/textarea')

    getData.send_keys("heelo")

    print(getData.get_attribute('value'))

    with open("data.json", 'w') as file:
        json.dump(getData.get_attribute('value'), file, indent=4)

    time.sleep(5)