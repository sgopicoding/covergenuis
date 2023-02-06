from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class RentalCoverHome:

    def __int__(self, browser):
        self.browser = browser

        self.input_country_textbox_xpath = "//input[@placeholder='Select or type a country']"
        self.from_date_picker_xpath = "//input[@id='QuoteForm_FromDate-datepicker']"
        self.from_date_select_xpath = "//*[contains(@class, 'ui-datepicker-today')]"
        self.to_date_picker_xpath = "//input[@id='QuoteForm_ToDate-datepicker']"
        self.to_date_select_xpath = "//*[contains(@class, 'ui-datepicker-today')]"
        self.vehicle_change_class = "QuoteForm-optionalField-change"
        self.vehicle_type_id = "QuoteForm_VehicleType"
        self.instant_quote_button_css = "button.QuoteForm-submit.Form-submit.btn.btn-warning.btn-lg.btn-block"

    def enter_country_name(self, country):
        self.browser.find_element(By.XPATH, self.input_country_textbox_xpath).click()
        self.browser.find_element(By.XPATH, self.input_country_textbox_xpath).send_keys(country)

    def select_from_date(self):
        self.browser.find_element(By.XPATH, self.from_date_picker_xpath).click()
        self.browser.find_element(By.XPATH, self.from_date_select_xpath).click()

    def select_to_date(self):
        self.browser.find_element(By.XPATH, self.to_date_picker_xpath).click()
        self.browser.find_element(By.XPATH, self.to_date_select_xpath).click()

    def select_vehicle(self, vehicle_type):
        self.browser.find_element(By.CLASS_NAME, self.vehicle_change_class)[1].click()
        select_vehicle = Select(self.browser.find_element(By.ID, self.vehicle_type_id)
        select_vehicle.select_by_value(vehicle_type)

    def click_instant_quote_button(self):
        self.browser.find_element(By.CSS_SELECTOR, self.instant_quote_button_css).click()

