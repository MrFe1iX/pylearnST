from model.group import Group
from model.contact import Contact
import random
from fixture.orm import ORMFixture

db = ORMFixture(host="127.0.0.1", database="addressbook", user="root", password="")


def test_add_contact_to_group(app):
    if len(app.contact.get_user_list()) == 0:
        app.contact.add_new_user(Contact(firstname="New", lastname="OldBoy"))
    if len(app.group.get_group_list()) == 0:
        app.group.create(Group(name="LOLOLOL", header="ssda", footer="sasdas"))
    user_list = db.get_user_list()
    group_list = db.get_group_list()
    user_id = random.choice(user_list).id
    group_id = random.choice(group_list).id
    app.contact.add_user_to_group(user_id, group_id)


