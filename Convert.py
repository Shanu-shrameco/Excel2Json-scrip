import os
import random
import time
import json

import keyboard
import pyautogui
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

def convertData():
    driver = webdriver.Chrome()
    driver.get('https://codebeautify.org/excel-to-json')

    time.sleep(2)

    # press upload file
    driver.find_element(By.XPATH, '//*[@id="app"]/div[3]/div/div[1]/div[1]/div/button[2]').click()

    time.sleep(2)

    pyautogui.hotkey('ctrl', 'l')

    time.sleep(1)

    pyautogui.write("/home/shanu/codes/python/Excel2Json/separated_columns.xlsx")

    time.sleep(1)

    pyautogui.press('enter')
    time.sleep(5)


    print("clicked")




    # get the output data and save it in json file
    driver.find_element(By.XPATH, '//*[@id="app"]/div[3]/div/div[1]/div[1]/div/button[3]').click()

    time.sleep(1)

    pyautogui.write("data.json")

    time.sleep(1)

    pyautogui.press('enter')
    time.sleep(2)


    print("done")

