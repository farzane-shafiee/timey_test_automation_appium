
class LoginComponyPageLocators:
    def __init__(self):
        self.locators = {
            "next_button": 'ir.timey.app:id/next',
            "username_input": 'ir.timey.app:id/etxt_username',
            "submit_username_button": 'ir.timey.app:id/txt_title',
            "otp_page_label": '//*[@text="کد ارسالی به ایمیل را وارد کنید"]',
            "otp_input": 'ir.timey.app:id/etxt_verification_code',
            "test_otp_button": 'ir.timey.app:id/btn_confirm',

        }

    def __getitem__(self, index):
        return self.locators[index]