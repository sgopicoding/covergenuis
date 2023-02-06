from selenium.webdriver.common.by import By


class RentalPolicyPayment:

    def __int__(self, browser):
        self.browser = browser

        self.policy_info_xpath = "//h2[@id='policy-inclusions' and contains(text(),'Policy Information & Payment')]"

    def check_policy_information(self):
        self.browser.find_element(By.XPATH, self.policy_info_xpath)
