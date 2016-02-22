# -*- coding: utf-8 -*-

from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains


"""
    PageModel - Abstract superclass for model pages content
"""


class PageModel(object):
    """
        Defining the abstract class
    """

    __DEFAULT_MAX_TIME_WAIT_HIGHT = 60
    __DEFAULT_MAX_TIME_WAIT_MEDIUM = 30
    __DEFAULT_MAX_TIME_WAIT_LOW = 10
    __DEFAULT_MAX_TIME_WAIT_MINOR = 5

    def __initWaiters__(self):
        """
            Default max time to wait for elements and page
        """
        self._waitHight = WebDriverWait(self._driver, self.__DEFAULT_MAX_TIME_WAIT_HIGHT)
        self._waitMedium = WebDriverWait(self._driver, self.__DEFAULT_MAX_TIME_WAIT_MEDIUM)
        self._waitLow = WebDriverWait(self._driver, self.__DEFAULT_MAX_TIME_WAIT_LOW)
        self._waitMinor = WebDriverWait(self._driver, self.__DEFAULT_MAX_TIME_WAIT_MINOR)

    def __init__(self, driv):
        """
            Constructs a PageModel with default properties, driver and Waiters
        """
        self._driver = driv
        self.__initWaiters__()

    def _isLoaded(self, page):
        """
            Check if the page is loaded
        """
        url = self._driver.getCurrentUrl()
        try:
            assert "Not on the issue entry page: " + url, url == page
        except AssertionError:
            raise AssertionError

    def _isDisplayed(self, element_reference):
        element = self._getWebElement(element_reference)
        return element.is_displayed()

    def _checkEqual(self, string1, string2):
        try:
            assert string1 == string2
        except AssertionError:
            raise AssertionError

    def __getByLocator__(self, element_reference):
        """
            Gets By Locator
            :param element_reference: Reference to a web elements by ID or XPATH
            :return By locator to this element
        """
        if "//" in element_reference:
            return By.XPATH, element_reference
        else:
            return By.ID, element_reference

    def waitForElementLoaded(self, element_reference, ):
        """
            Implements a time wait for specified element
            :param element_reference: Element for wait its load
        """
        try:
            until = self._waitLow.until(EC.visibility_of_element_located(self.__getByLocator__(element_reference)))
        except TimeoutException:
            if element_reference != "submit_phase2":
                raise Exception('Wait for element: Element not found [ELEMENT: %s]. <Method called from: %s>', str(element_reference), self.getNameClassPretty(str(self)))

    def wait_For_Element_is_not_Loaded(self, element_reference):
        until = self._waitLow.until(EC.invisibility_of_element_located(self.__getByLocator__(element_reference)))

    def _getWebElement(self, element_reference):
        """
            Gets Web Element referenced, specified its correct type
            :param element_reference: Reference to a web elements
            :return Formed Web Element, if exit in web page
        """
        self.waitForElementLoaded(element_reference)
        locator = self.__getByLocator__(element_reference)
        return self._driver.find_element(locator[0], locator[1])

    def _typeInElement(self, element_reference, value):
        """
            Types a text in specified text area by its reference
            :param element_reference: web element reference. XPATH or ID
            :param value: Text to type
        """
        element = self._getWebElement(element_reference)
        element.clear()
        element.send_keys(value)

    def _getText(self, element_reference):
        return self._getWebElement(element_reference).text

    def _clickOnElement(self, element_reference):
        """
            Clicks on specified elements by its reference
        :rtype : object
            :param element_reference: web element reference. XPATH or ID
        """
        element = self._getWebElement(element_reference)
        element.click()

    def _clickOnElementDropdownMenu(self, menu_reference, element_reference):
        element = self._getWebElement(menu_reference)
        hov = ActionChains(self._driver).move_to_element(element)
        hov.perform()
        element2 = self._getWebElement(element_reference)
        element2.click()

    def _selectValueList(self, element_reference, zone):
        """
            Selects a specified elements from a list by its reference
            :param element_reference: web element reference. XPATH or ID
        """
        '''
        # Esta es la implementacion original que hizo Juan, por si hay que volver a recuperarla la dejo comentada
        list = self._getWebElement(element_reference)
        list.click()
        for option in list.find_elements_by_tag_name('option'):
            if option.text == 'Europe/London' :
                option.click
                break
        '''
        self._select_value_list_option_by_text(element_reference, zone)

    def _select_value_list_option_by_value(self, element_reference, option_):
        """
            Selects a specified elements from a list by its reference
            :param element_reference: web element reference. XPATH or ID
        """
        # Ponemos un doble click sobre la lista de opciones pues con uno solo no parece funcionar correctamente.

        list = self._getWebElement(element_reference)
        list.click()

        list = self._getWebElement(element_reference)
        list.click()

        select = Select(list)
        select.select_by_value(option_)

        AC = ActionChains(self._driver)
        AC.click()

    def _select_value_list_option_by_text(self, element_reference, option_):
        """
            Selects a specified elements from a list by its reference
            :param element_reference: web element reference. XPATH or ID
        """
        # Ponemos un doble click sobre la lista de opciones pues con uno solo no parece funcionar correctamente.

        list = self._getWebElement(element_reference)
        list.click()

        list = self._getWebElement(element_reference)
        list.click()

        select = Select(list)
        select.select_by_visible_text(option_)

        AC = ActionChains(self._driver)
        AC.click()

    # def _text_in_element(self, element_reference):
    #     self.waitForElementLoaded(element_reference)
    #     locator = self.__getByLocator__(element_reference)
    #     if element_reference == ".//*[@id='id_name']" or element_reference == ".//*[@id='id_surname']":
    #         return self._driver.find_element(locator[0], locator[1]).get_attribute('value')
    #     elif element_reference == ".//*[@id='id_timezone']":
    #         return Select(self._driver.find_element(locator[0], locator[1])).first_selected_option.text
    #     else:
    #         return self._driver.find_element(locator[0], locator[1]).text

    def is_text_correct(self, text, element):
        try:
            web_text = self._getText(element)
            print web_text
            web_text.index(text)
            return True
        except ValueError:
            print "The text of the web is not as expected"
        except Exception:
            print "Exception, 'I should see' fail"
        return False
