# -*- coding: utf-8 -*-

import unittest

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from pages.keys_ssh_page import KeysSshPage
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from commons.utils import *


class TestClaveSSH(unittest.TestCase):

    generalProp = generalProperties()

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get(self.generalProp["url"])
        self.assertIn("Cloud Servers", self.driver.title)

    def test_clave_ssh_cloud_server(self):
        username = self.generalProp["user"]
        password = self.generalProp["pass"]
        keyName = self.generalProp["keyName"]

        login = LoginPage(self.driver)
        dashboard = DashboardPage(self.driver)
        keys_ssh = KeysSshPage(self.driver)

        # Login
        login.type_user_name(username)
        login.type_user_pass(password)
        login.click_on_send()

        # Close tour dialog is displayed
        dashboard.close_tour_dialog()

        # I'm in dashboard page
        assert dashboard.check_dashboard_page()

        # Wait for dialog window is not loaded
        dashboard.wait_element_dialog_window()

        # Click on keys ssh
        dashboard.click_keys_ssh()
        # I'm in keys ssh page
        assert keys_ssh.check_keys_page()

        # Create new key ssh
        keys_ssh.click_create_new_key()
        keys_ssh.type_key_name(keyName)

        # Click autogenerate key
        keys_ssh.click_autogenerate_key()
        # Wait to complete the field
        assert keys_ssh.wait_write_key_ssh()

        keys_ssh.confirm_create_new_key_dialog()

        # Logout
        dashboard.logout()

    def tearDown(self):
        self.driver.close()

    if __name__ == "__main__":
        unittest.main()
