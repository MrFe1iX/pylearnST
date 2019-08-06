from model.group import Group
from model.contact import Contact
import random
import pytest
from fixture.orm import ORMFixture

db = ORMFixture(host="127.0.0.1", database="addressbook", user="root", password="")


def test_del_contact_from_group(app, db, orm):
    if len(app.contact.get_user_list()) == 0:
        app.contact.add_new_user(Contact(firstname="New", lastname="OldBoy"))
    if len(app.group.get_group_list()) == 0:
        app.group.create(Group(name="LOLOLOL", header="ssda", footer="sasdas"))
    if len(db.get_groups_with_contacts()) == 0:
        contact_id = random.choice(db.get_contact_list()).id
        group_id = random.choice(db.get_group_list()).id
        app.contact.add_contact_to_group(contact_id, group_id)
    group_id = random.choice(db.get_groups_with_contacts()).id
    contact_id = random.choice(orm.get_contacts_in_group(Group(id=group_id))).id
    with pytest.allure.step('Удаление контакта'):
        app.contact.delete_contact_from_group(group_id)
        assert db.get_contact_by_id(contact_id) not in orm.get_contacts_in_group(Group(id=group_id))