import time

from selenium.common import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from helpers import retrieve_phone_code

class UrbanRoutesPage:
    FROM_LOCATOR = (By.ID, 'from')
    TO_LOCATOR = (By.ID, 'to')
    CALL_A_TAXI_LOCATOR = (By.XPATH, '//button[contains(text(), "Call a taxi")]')
    CALL_A_SUPPORTIVE_PLAN_LOCATOR = (By.XPATH, '//div[contains(text(), "Supportive")]')
    SUPPORTIVE_PLAN_CARD_PARENT = (By.XPATH, '//div[contains(text(), "Supportive")]//..')
    ACTIVE_PLAN = (By.XPATH, '//div[@class="tcard active"]//div[@class="tcard-title"]')
    PHONE_NUMBER_BUTTON = (By.XPATH, "//div[@class='np-text']")
    PHONE_NUMBER_FIELD = (By.XPATH, "//input[@id='phone']")
    PHONE_NUMBER_NEXT_BUTTON = (By.XPATH, "//button[text()='Next']")
    CODE_FIELD = (By.XPATH, "//input[@id='code']")
    CONFIRM_BUTTON = (By.XPATH, "//button[@type='submit' and text()='Confirm']")
    PAYMENT_METHOD_BUTTON = (By.XPATH, "//div[@class='pp-value-text']")
    ADD_CARD_BUTTON = (By.XPATH, "//div[@class='pp-title' and text()='Add card']")
    CARD_NUMBER_FIELD = (By.XPATH, "//input[@id='number']")
    CVV_NUMBER_FIELD = (By.XPATH, "//input[@class='card-input' and @placeholder='12']")
    ADDING_A_CARD_TITLE = (By.XPATH, "//div[@class='head' and text()='Adding a card']")
    LINK_BUTTON = (By.XPATH, "//button[@type='submit' and text()='Link']")
    ADD_DRIVER_COMMENT = (By.XPATH, "//input[@id='comment']")
    BLANKET_HANKERCHIEF_CHECK = (By.XPATH, "//input[@class='switch-input']")
    BLANKET_HANKERCHIEF_SLIDER_ROUND = (By.XPATH, "//span[@class='slider round']")
    ICE_CREAM_COUNTER_VALUE = (By.XPATH, "//div[@class='counter-value']")
    ICE_CREAM_COUNTER_PLUS = (By.XPATH, "//div[@class='counter-plus' and text()='+']")
    NEXT_BUTTON = (By.XPATH, "//button[@type='button' and @class='smart-button']")
    CAR_SEARCH_MODAL = (By.XPATH, "//div[text()='Car search']")


    def __init__(self, driver):
        self.driver = driver
        #self.wait = WebDriverWait(self.driver, 5)  # Create wait once in constructor

    def enter_from_location(self, from_text):
        from_field = WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.FROM_LOCATOR))
        #from_field.clear()  # Clear any existing text
        from_field.send_keys(from_text)

    def enter_to_location(self, to_text):
        to_field = self.driver.find_element(*self.TO_LOCATOR)
        #to_field.clear()  # Clear any existing text
        to_field.send_keys(to_text)

    def click_call_a_taxi(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(self.CALL_A_TAXI_LOCATOR))
        self.driver.find_element(*self.CALL_A_TAXI_LOCATOR).click()

    def select_supportive_plan(self):
        if self.driver.find_element(*self.SUPPORTIVE_PLAN_CARD_PARENT).get_attribute("class") != "tcard active":
            supportive_plan = WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(self.CALL_A_SUPPORTIVE_PLAN_LOCATOR))
            self.driver.execute_script("arguments[0].scrollIntoView();", supportive_plan)
            supportive_plan.click()

    def get_selected_plan(self):
        plan = self.driver.find_element(*self.ACTIVE_PLAN).text
        return plan

    def get_from_location(self):
        from_field = self.driver.find_element(*self.FROM_LOCATOR).get_property('value')
        return from_field

    def get_to_location(self):
        to_field = self.driver.find_element(*self.TO_LOCATOR).get_property('value')
        return to_field

    def click_phone_number_button(self):
        self.driver.find_element(*self.PHONE_NUMBER_BUTTON).click()

    def enter_phone_number(self, phone_number):
        self.driver.find_element(*self.PHONE_NUMBER_FIELD).send_keys(phone_number)

    def click_next_button(self):
        self.driver.find_element(*self.PHONE_NUMBER_NEXT_BUTTON).click()

    def enter_code(self, code):
        self.driver.find_element(*self.CODE_FIELD).send_keys(code)

    def click_confirm_button(self):
        self.driver.find_element(*self.CONFIRM_BUTTON).click()

    def get_saved_phone_number(self):
        return self.driver.find_element(*self.PHONE_NUMBER_BUTTON).text

    def click_payment_method(self):
        self.driver.find_element(*self.PAYMENT_METHOD_BUTTON).click()

    def click_add_card(self):
        self.driver.find_element(*self.ADD_CARD_BUTTON).click()

    def enter_card_number(self, card_number):
        self.driver.find_element(*self.CARD_NUMBER_FIELD).send_keys(card_number)

    def enter_cvv_number(self, cvv_number):
        self.driver.find_element(*self.CVV_NUMBER_FIELD).send_keys(cvv_number)

    def click_adding_a_card_title(self):
        self.driver.find_element(*self.ADDING_A_CARD_TITLE).click()

    def click_link_button(self):
        self.driver.find_element(*self.LINK_BUTTON).click()

    def get_payment_method(self):
        return self.driver.find_element(*self.PAYMENT_METHOD_BUTTON).text

    def enter_driver_comment(self, comment):
        self.driver.find_element(*self.ADD_DRIVER_COMMENT).send_keys(comment)

    def get_driver_comment(self):
        return self.driver.find_element(*self.ADD_DRIVER_COMMENT).get_property('value')

    def get_blanket_hankerchief_state(self):
        return self.driver.find_element(*self.BLANKET_HANKERCHIEF_CHECK).get_property('checked')

    def click_blanket_hankerchief_button_round(self):
        self.driver.find_element(*self.BLANKET_HANKERCHIEF_SLIDER_ROUND).click()

    def click_ice_cream_counter_plus(self, amount):
        for i in range(amount):
            self.driver.find_element(*self.ICE_CREAM_COUNTER_PLUS).click()

    def get_ice_cream_amount(self):
        return self.driver.find_element(*self.ICE_CREAM_COUNTER_VALUE).text

    def next_button(self):
        self.driver.find_element(*self.NEXT_BUTTON).click()

    def get_car_search_display_status(self):
        return self.driver.find_element(*self.CAR_SEARCH_MODAL).is_displayed()

    def set_route(self, from_text, to_text):
        self.enter_from_location(from_text)
        self.enter_to_location(to_text)
        self.click_call_a_taxi()

