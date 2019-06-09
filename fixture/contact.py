
class ContactHelper:

    def __init__(self, app):
        self.app = app

    def add_user_info(self, contact):
        wd = self.app.wd
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
