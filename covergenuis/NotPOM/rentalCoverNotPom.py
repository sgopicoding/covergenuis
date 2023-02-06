from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import unittest


class RentalQuote(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.browser = webdriver.Chrome()
        cls.browser.implicitly_wait(10)
        cls.browser.maximize_window()

    def test_rental_instant_quote(self):
        self.browser.get('https://www.rentalcover.com')
        input_country = self.browser.find_element(By.XPATH, "//input[@placeholder='Select or type a country']")
        input_country.click()
        input_country.send_keys("United States")
        self.browser.find_element(By.XPATH, "//input[@id='QuoteForm_FromDate-datepicker']").click()
        self.browser.find_element(By.XPATH, "//*[contains(@class, 'ui-datepicker-today')]").click()
        self.browser.find_element(By.XPATH, "//input[@id='QuoteForm_ToDate-datepicker']").click()
        self.browser.find_element(By.XPATH, "//*[contains(@class, 'ui-datepicker-today')]").click()
        self.browser.find_elements(By.CLASS_NAME, 'QuoteForm-optionalField-change')[1].click()
        select_vehicle_type = Select(self.browser.find_element(By.ID, 'QuoteForm_VehicleType'))
        select_vehicle_type.select_by_value('car')
        self.browser.find_element(By.CSS_SELECTOR,
                                  'button.QuoteForm-submit.Form-submit.btn.btn-warning.btn-lg.btn-block').click()
        self.browser.find_element(By.XPATH,
                                  "//h2[@id='policy-inclusions' and contains(text(),'Policy Information & Payment')]")

    @classmethod
    def tearDownClass(cls):
        cls.browser.close()
        cls.browser.quit()
