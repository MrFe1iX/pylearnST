

class GroupHelper:

    def __init__(self, app):
        self.app = app

    def fill_group_form(self, group):
        wd = self.app.wd
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.footer)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def create(self, group):
        wd = self.app.wd
        # Нажать на новая группа и заполнение
        self.open_group_page()
        wd.find_element_by_name("new").click()
        self.fill_group_form(group)
        # Сохранить
        wd.find_element_by_name("submit").click()
        self.return_to_group_page()

    def edit_first(self, new_group_data):
        wd = self.app.wd
        self.open_group_page()
        self.select_first_group()
        wd.find_element_by_name("edit").click()
        self.fill_group_form(new_group_data)
        # Сохранить
        wd.find_element_by_name("update").click()
        self.return_to_group_page()

    def select_first_group(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def open_group_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0):
            wd.find_element_by_link_text("groups").click()

    def return_to_group_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

    def del_first_group(self):
        wd = self.app.wd
        self.open_group_page()
        self.select_first_group()
        wd.find_element_by_name("delete").click() 
        self.return_to_group_page()

    def count(self):
        wd = self.app.wd
        self.open_group_page()
        return len(wd.find_elements_by_name("selected[]"))