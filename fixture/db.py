import pymysql.cursors
from model.group import Group
from model.contact import Contact


class DbFixture:

    def __init__(self, host, database, user, password):
        self.host = host
        self.name = database
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=database, user=user, password=password, autocommit=True)

    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("SELECT group_id, group_name, group_header, group_footer FROM group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()

        return list

    def get_user_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("SELECT id, firstname, lastname FROM addressbook where deprecated='0000-00-00 00:00:00' ")
            for row in cursor:
                (id, firstname, lastname) = row
                list.append(Contact(id=str(id), firstname=firstname, lastname=lastname))
        finally:
            cursor.close()

        return list

    def get_groups_with_contacts(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id from address_in_groups")
            for row in cursor:
                (id,) = row
                list.append(Group(id=str(id)))

        finally:
            cursor.close()
        return list

    def disconect(self):
        self.connection.close()
