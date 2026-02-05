class SignupPage:

    def __init__(self, page):
        self.page = page
        self.first_name = "#first-name"
        self.last_name = "#last-name"
        self.postal_code = "#postal-code"
        self.continue_btn = "#continue"

    def fill_details(self, fname, lname, zip_code):
        self.page.fill(self.first_name, fname)
        self.page.fill(self.last_name, lname)
        self.page.fill(self.postal_code, zip_code)

    def click_continue(self):
        self.page.click(self.continue_btn)
