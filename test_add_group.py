# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException


class TestAddGroup(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def test_add_group(self):
        wd = self.wd
        # Открыта страница
        wd.get("http://localhost/addressbook/")
        # Логин
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys("admin")
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys("secret")
        wd.find_element_by_xpath("//input[@value='Login']").click()
        # Открыть группы
        wd.find_element_by_link_text("groups").click()
        # Нажать на новая группа и заполнение
        wd.find_element_by_name("new").click()
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys("Testing")
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys("OLOLOLOLOLO")
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys("SUPER CLASS")
        # Сохранить
        wd.find_element_by_name("submit").click()
        wd.find_element_by_link_text("group page").click()
        # Выйти
        wd.find_element_by_link_text("Logout").click()

    def tearDown(self):
        self.wd.quit()

