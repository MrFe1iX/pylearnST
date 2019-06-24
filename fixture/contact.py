from time import sleep
from model.contact import Contact


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def fill_user_form(self, contact):
        wd = self.app.wd
        self.edit_field_value("firstname", contact.firstname)
        self.edit_field_value("middlename", contact.middlename)
        self.edit_field_value("lastname", contact.lastname)
        self.edit_field_value("nickname", contact.nick)
        self.edit_field_value("email", contact.email)
        self.fill_user_form_day(contact.day)
        self.fill_user_form_month(contact.month)
        self.edit_field_value("byear", contact.year)
        self.edit_field_value("address", contact.address)

    def fill_user_form_day(self, field_day):
        wd = self.app.wd
        if field_day is not None:
            wd.find_element_by_css_selector("option[value=" + "'" + str(field_day) + "'" + "]").click()

    def fill_user_form_month(self, field_month):
        wd = self.app.wd
        month_book = {1: "January", 2: "February", 3: "March",
                      4: "April", 5: "May", 6: "June",
                      7: "July", 8: "August", 9: "September", 10: "October",
                      11: "November", 12: "December"
                      }
        if field_month is not None:
            wd.find_element_by_css_selector("option[value=" + month_book[field_month] + "]").click()

    def edit_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def add_new_user(self, contact):
        wd = self.app.wd
        # Click on add user
        wd.find_element_by_link_text("add new").click()
        self.fill_user_form(contact)
        # Save
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def edit_user_info(self, new_user_data):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_css_selector("img[alt='Edit']").click()
        self.fill_user_form(new_user_data)
        # Save
        wd.find_element_by_name("update").click()
        self.app.open_home_page()

    def del_first_user(self):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        wd.find_element_by_css_selector("div.msgbox")
        self.app.open_home_page()

    def del_all_user(self):
        wd = self.app.wd
        wd.find_element_by_id("MassCB").click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        self.app.open_home_page()

    def count(self):
        wd = self.app.wd
        self.app.open_home_page()
        return len(wd.find_elements_by_css_selector("img[alt='Edit']"))

    def get_user_list(self):
        wd = self.app.wd
        self.app.open_home_page()
        user = []
        for element in wd.find_elements_by_css_selector("tr[name='entry']"):
            cells = element.find_elements_by_tag_name("td")
            first_n = cells[2].text
            last_n = cells[1].text
            id = element.find_element_by_name("selected[]").get_attribute("value")
            user.append(Contact(id=id, firstname=first_n, lastname=last_n))

        return user
