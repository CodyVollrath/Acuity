import time

import utils.ImageHandling as ih
from models.visit_sub_type import VisitSubType
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import cv2
import pyautogui
import time
import keyboard


class AcuityImporter:
    def __init__(self):
        self.url_login = 'https://nectarine-pufferfish-thsz.squarespace.com/config/scheduling/appointments.php?action=newAppointmentType'
        self.webdriver_path = './drivers/msedgedriver.exe'
        options = webdriver.EdgeOptions()
        options.page_load_strategy = 'eager'
        self.driver = webdriver.Edge(options)
        self.nameFieldImage = cv2.imread('./drivers/nameField_ss.png')
        self.submitBtn = cv2.imread('./drivers/submitBtn.png')

    def login(self, username, password):
        self.driver.get(self.url_login)
        element_present = EC.presence_of_element_located((By.ID, 'login-button'))
        WebDriverWait(self.driver, 5).until(element_present)
        input_fields = self.driver.find_elements(By.TAG_NAME, 'input')
        email_field = input_fields[0]
        password_field = input_fields[1]
        email_field.send_keys(username)
        password_field.send_keys(password)
        login_btn = self.driver.find_element(By.ID, 'login-button')
        login_btn.click()

    def find_location(self, name):
        self.perform_click_and_type(124, 509, name)
        # result = cv2.matchTemplate(windowSs, self.nameFieldImage, cv2.TM_CCOEFF_NORMED)
        # min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        # top_left = max_loc
        # x, y = top_left
        # self.driver.execute_script(f'window.scrollTo({479}, {361});')
        # time.sleep(1)
        # self.driver.find_element(By.XPATH, '//body').click()  # Click to focus on the page
        # actions = webdriver.ActionChains(self.driver)
        # actions.move_to_element_with_offset(self.driver.find_element(By.XPATH, '//body'), 479, 361)
        # actions.click()
        # actions.perform()
        # input_field = self.driver.switch_to.active_element
        # input_field.send_keys('your_input_data')

    def input_appointment_types(self, subtypes: set[VisitSubType]):
        input('waiting')
        self.driver.get(self.url_login)
        element_present = EC.presence_of_element_located((By.ID, 'typekit-preview-script'))
        WebDriverWait(self.driver, 100).until(element_present)
        input('waiting')
        for subtype in subtypes:
            self.find_location(f'{subtype.abbreviation} - {subtype.name} - {subtype.id}')
            time.sleep(2)
        input("Waiting")
        # nameField = self.driver.find_element(By.ID, 'name')
        # nameField.send_keys(name)
        # submit_btn = self.driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]')
        # submit_btn.click()
        # input('waiting')

    def perform_click_and_type(self, x, y, text_to_type):
        try:
            # Move the mouse cursor to the specified position
            pyautogui.moveTo(x, y, duration=0.5)

            # Click at the specified position
            pyautogui.click()

            # Pause for a moment before typing
            time.sleep(1)

            # Type the specified text
            keyboard.write(text_to_type)
            pyautogui.moveTo(894,1002)
            pyautogui.click()
            pyautogui.click()
            pyautogui.click()
            pyautogui.click()
            pyautogui.moveTo(168,913)
            pyautogui.click()
            time.sleep(2)
            pyautogui.moveTo(146,457)
            pyautogui.click()

        except Exception as e:
            print(f"Error: {e}")