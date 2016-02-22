# -*- coding: utf-8 -*-

from commons.page_model import PageModel


class LoginPage(PageModel):

    USERNAME = "username"
    PASSWORD = "password"
    #LOGIN = "login"
    #EMAIL = "email"
    BUTTON_SEND = "btnLogin"
    #FORGOT_PASSWORD = ".//*[@id='loginForm']/footer/div/a"
    #FORGOT_PASSWORD_DIALOG = ".//*[@id='forgotten-password-dialog']/div"
    #CLOSE_PASSWORD_DIALOG = ".//*[@id='forgotten-password-dialog']/div/div[1]"
    #CANCEL_PASSWORD_DIALOG = ".//*[@id='forgottenPasswordForm']/footer/button[2]"
    #BUTTON_SEND_FORGOT_PASSWORD_DIALOG = ".//*[@id='forgottenPasswordForm']/footer/button[1]"
    TERMS_OF_USE = ".//*[@id='footer']/div/a[1]"
    IMAGE_VDC = "//html/body/div[1]/div[1]/div[2]/h2"

    def check_login_page(self):
        return super(LoginPage, self)._getText(self.IMAGE_VDC)

    def type_user_name(self, username):
        super(LoginPage, self)._typeInElement(self.USERNAME, username)

    def type_user_pass(self, password):
        super(LoginPage, self)._typeInElement(self.PASSWORD, password)

    def click_on_send(self):
        super(LoginPage, self)._clickOnElement(self.BUTTON_SEND)
"""
    def fotgot_password(self):
        super(LoginPage, self)._clickOnElement(self.FORGOT_PASSWORD)

    def close_password_dialog(self):
        super(LoginPage, self)._clickOnElement(self.CLOSE_DIALOG_WINDOW)

    def cancel_password_dialog(self):
        super(LoginPage, self)._clickOnElement(self.CANCEL_PASSWORD_DIALOG)

    def type_user_login_password_dialog(self, login):
        super(LoginPage, self)._typeInElement(self.LOGIN, login) #login = self.generalProp["login"]

    def type_user_email_password_dialog(self, email):
        super(LoginPage, self)._typeInElement(self.EMAIL, email) #email = self.generalProp["email"]

    def click_on_send_password_dialog(self):
        super(LoginPage, self)._clickOnElement(self.BUTTON_SEND_FORGOT_PASSWORD_DIALOG)

    def click_on_terms_of_use(self):
        super(LoginPage, self)._clickOnElement(self.TERMS_OF_USE)
        """