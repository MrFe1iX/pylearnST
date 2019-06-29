import re
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
        self.edit_field_value("address", contact.address)
        self.edit_field_value("home", contact.homephone)
        self.edit_field_value("mobile", contact.mobilephone)
        self.edit_field_value("work", contact.workphone)
        self.edit_field_value("fax", contact.fax)
        self.fill_user_form_day(contact.day)
        self.fill_user_form_month(contact.month)
        self.edit_field_value("byear", contact.year)


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
        self.user_cache = None

    def edit_rand_user_info(self, new_user_data, index):
        wd = self.app.wd
        self.select_some_edit_user(index)
        self.fill_user_form(new_user_data)
        # Save
        wd.find_element_by_name("update").click()
        self.app.open_home_page()
        self.user_cache = None

    def edit_user_info(self, new_user_data):
        wd = self.app.wd
        self.select_some_edit_user(0)
        self.fill_user_form(new_user_data)
        # Save
        wd.find_element_by_name("update").click()
        self.app.open_home_page()
        self.user_cache = None

    def select_some_edit_user(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_elements_by_css_selector("img[alt='Edit']")[index].click()

    def del_some_user(self, index):
        wd = self.app.wd
        self.select_some_user(index)
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        sleep(0.3)
        wd.find_element_by_css_selector("div.msgbox")
        self.app.open_home_page()
        self.user_cache = None

    def del_first_user(self):
        wd = self.app.wd
        self.select_some_user(0)
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        sleep(0.3)
        wd.find_element_by_css_selector("div.msgbox")
        self.app.open_home_page()
        self.user_cache = None

    def select_some_user(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_elements_by_name("selected[]")[index].click()

    def del_all_user(self):
        wd = self.app.wd
        wd.find_element_by_id("MassCB").click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        self.app.open_home_page()
        self.user_cache = None

    def count(self):
        wd = self.app.wd
        self.app.open_home_page()
        return len(wd.find_elements_by_css_selector("img[alt='Edit']"))

    user_cache = None

    def get_user_list(self):
        if self.user_cache is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.user_cache = []
            for element in wd.find_elements_by_css_selector("tr[name='entry']"):
                cells = element.find_elements_by_tag_name("td")
                first_n = cells[2].text
                last_n = cells[1].text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                all_phones = cells[5].text.splitlines()
                self.user_cache.append(Contact(id=id, firstname=first_n, lastname=last_n,
                                               homephone=all_phones[0], mobilephone=all_phones[1],
                                               workphone=all_phones[2]))

        return list(self.user_cache)

    def open_user_to_edit_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_user_view_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_user_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_user_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        # fax = wd.find_element_by_name("fax").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id=id,
                       homephone=homephone, workphone=workphone, mobilephone=mobilephone)

    def get_user_from_view_page(self, index):
        wd = self.app.wd
        self.open_user_view_by_index(index)
        text = wd.find_element_by_id("content").text
        homephone = re.search("H: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        return Contact(homephone=homephone, workphone=workphone, mobilephone=mobilephone)
