from model.group import Group
from model.contact import Contact
import random
import pytest
from fixture.orm import ORMFixture


def test_add_contact_to_group(app, db, orm):
    if len(app.contact.get_user_list()) == 0:
        app.contact.add_new_user(Contact(firstname="New", lastname="OldBoy"))
    if len(app.group.get_group_list()) == 0:
        app.group.create(Group(name="LOLOLOL", header="ssda", footer="sasdas"))
    user_list = db.get_user_list()
    group_list = db.get_group_list()
    user_id = random.choice(user_list).id
    group_id = random.choice(group_list).id
    app.contact.add_user_to_group(user_id, group_id)
    assert db.get_user_by_id(user_id) in orm.get_contacts_in_group(Group(id=group_id))


