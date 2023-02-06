from selenium import webdriver
import unittest
from covergenuis.Pages.rentalCoverHome import RentalCoverHome
from covergenuis.Pages.rentalPolicyPayment import RentalPolicyPayment


class RentalQuote(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.browser = webdriver.Chrome()
        cls.browser.implicitly_wait(10)
        cls.browser.maximize_window()

    def test_rental_instant_quote(self):

        self.browser.get("https://www.rentalcover.com")

        coverhomepage = RentalCoverHome(self.browser)
        coverhomepage.enter_country_name("United States")
        coverhomepage.select_from_date()
        coverhomepage.select_to_date()
        coverhomepage.select_vehicle("car")
        coverhomepage.click_instant_quote_button()

        policypaymentpage = RentalPolicyPayment(self.browser)
        policypaymentpage.check_policy_information()

    @classmethod
    def tearDownClass(cls):
        cls.browser.close()
        cls.browser.quit()
