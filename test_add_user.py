# -*- coding: utf-8 -*-
from selenium import webdriver
from obj_class import Contact
import unittest


class TestAddUser(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def test_add_user(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.add_user_info(wd, Contact(firstname="Test", middlename="OlO", lastname="Testovich", nick="tes", email="test@test.ru",
                           address="Moskovskaz 12", month=2, day="10", year="1984"))
        self.logout(wd)

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def add_user_info(self, wd, contact):
        month_book = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June",
                      7: "July", 8: "August", 9: "September", 10: "October", 11: "November", 12: "December"
                      }
        # Click on add user
        wd.find_element_by_link_text("add new").click()
        # Fill
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(contact.middlename)
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(contact.nick)
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.email)
        wd.find_element_by_css_selector("option[value=" + "'" + str(contact.day) + "'" + "]").click()
        wd.find_element_by_name("bmonth").click()
        wd.find_element_by_css_selector("option[value=" + month_book[contact.month] + "]").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(contact.year)
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact.address)
        # Save
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/")

    def login(self, wd, username, password):
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
