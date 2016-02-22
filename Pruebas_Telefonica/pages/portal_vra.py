# -*- coding: utf-8 -*-

from commons.page_model import PageModel


class PortalVra(PageModel):

    #DIALOG_WINDOW = ".//*[@id='tour-dialog']/div"
    #CLOSE_DIALOG_WINDOW = ".//*[@id='tour-dialog']/div/div[1]"
    LOG_OUT = "//.//*[@id='SHELL_LOGOUT']"
    #KEYS_SSH = "//html/body/header/nav/div/ul/li[3]/a"
    #SHOW_HIDE_DETAILS = "//html/body/div[7]/div[2]/div[1]/div/a[1]"
    #MANAGE = "//html/body/div[7]/div[2]/div[1]/div/button"
    #DASHBOARD = ".//*[@id='dashboard']"

    def check_vra_page(self):
        return super(PortalVra, self)._getText(self.LOG_OUT)
    """
    def close_tour_dialog(self):
        if super(DashboardPage, self)._isDisplayed(self.DIALOG_WINDOW):
            super(DashboardPage, self)._clickOnElement(self.CLOSE_DIALOG_WINDOW)
    """
    def logout(self):
        super(PortalVra, self)._clickOnElement(self.LOG_OUT)

    """
    def click_keys_ssh(self):
         Click on keys ssh
        super(DashboardPage, self)._clickOnElement(self.KEYS_SSH)

    def wait_element_dialog_window(self):
        super(DashboardPage, self).wait_For_Element_is_not_Loaded(self.DIALOG_WINDOW)

    def click_show_hide_details(self):
        super(DashboardPage, self)._clickOnElement(self.SHOW_HIDE_DETAILS)

    def click_manage(self):
        super(DashboardPage, self)._clickOnElement(self.MANAGE)

    def go_dashbord_page(self):
        super(DashboardPage, self)._clickOnElement(self.DASHBOARD)
    """