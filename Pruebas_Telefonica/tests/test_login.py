# -*- coding: utf-8 -*-

import unittest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.portal_vra import PortalVra
from commons.utils import *
import time


class TestLogin(unittest.TestCase):

    generalProp = generalProperties()

    def setUp(self):

        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get(self.generalProp["url"])
        login = LoginPage(self.driver)
        assert login.check_login_page()

    def test_login_cloud_server(self):
        username = self.generalProp["user"]
        password = self.generalProp["pass"]

        login = LoginPage(self.driver)
        vra = PortalVra(self.driver)

        # Login
        login.type_user_name(username)
        login.type_user_pass(password)
        login.click_on_send()

        # Close tour dialog is displayed
        #dashboard.close_tour_dialog()

        # I'm in dashboard page
        assert vra.check_vra_page()

        # Logout
        vra.logout()

        #login.click_on_terms_of_use()
        #time.sleep(10)
        #self.assertIn("Centro de Ayuda: Condiciones de Servicios Móviles | Movistar, Chile", self.driver.title)

    def tearDown(self):
        self.driver.close()

    if __name__ == "__main__":
        unittest.main()
