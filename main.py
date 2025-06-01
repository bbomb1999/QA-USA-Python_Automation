import time

import data
import helpers
from selenium import webdriver
from pages import UrbanRoutesPage

class TestUrbanRoutes:
    @classmethod
    def setup_class(cls):
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(5)
        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
         print("Connected to the Urban Routes server")
        else:
            print("Cannot connect to Urban Routes. Check the server is on and still running")

    def test_set_route(self):
       self.driver.get(data.URBAN_ROUTES_URL)
       routes_page = UrbanRoutesPage(self.driver)
       routes_page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
       assert routes_page.get_to_location() == data.ADDRESS_TO
       assert routes_page.get_from_location() == data.ADDRESS_FROM

    def test_select_supportive_plan(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        routes_page.select_supportive_plan()
        assert routes_page.get_selected_plan() == 'Supportive'

    def test_fill_phone_number(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        routes_page.click_phone_number_button()
        routes_page.enter_phone_number(data.PHONE_NUMBER)
        time.sleep(2)
        routes_page.click_next_button()
        routes_page.enter_code(helpers.retrieve_phone_code(self.driver))
        routes_page.click_confirm_button()
        assert routes_page.get_saved_phone_number() == data.PHONE_NUMBER

    # no supportive plan for lines 34, 37, & 40.

    def test_fill_card_number(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        routes_page.click_payment_method()
        routes_page.click_add_card()
        routes_page.enter_card_number(data.CARD_NUMBER)
        routes_page.enter_cvv_number(data.CARD_CODE)
        routes_page.click_adding_a_card_title()
        routes_page.click_link_button()
        assert routes_page.get_payment_method() == "Card"

    def test_comment_for_driver(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        routes_page.enter_driver_comment(data.MESSAGE_FOR_DRIVER)
        assert routes_page.get_driver_comment() == data.MESSAGE_FOR_DRIVER

    def test_order_blanket_and_hankerchiefs(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        routes_page.select_supportive_plan()
        routes_page.click_blanket_hankerchief_button_round()
        assert routes_page.get_blanket_hankerchief_state()

    def test_order_2_ice_cream(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        routes_page.select_supportive_plan()
        amount = 2
        routes_page.click_ice_cream_counter_plus(amount)
        assert routes_page.get_ice_cream_amount() == str(amount)

    def test_car_search_model_appears(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        routes_page.select_supportive_plan()
        routes_page.enter_driver_comment(data.MESSAGE_FOR_DRIVER)
        routes_page.next_button()
        assert routes_page.get_car_search_display_status()


    @classmethod
    def teardown_class(cls):
        cls.driver.quit()