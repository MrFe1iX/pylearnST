# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_user(app, data_users):
    user = data_users
    old_user_list = app.contact.get_user_list()
    app.contact.add_new_user(user)
    assert len(old_user_list) + 1 == app.contact.count()
    new_user_list = app.contact.get_user_list()
    old_user_list.append(user)
    assert sorted(old_user_list, key=Contact.id_or_max) == sorted(new_user_list, key=Contact.id_or_max)


def test_add_user_json(app, json_users):
    user = json_users
    old_user_list = app.contact.get_user_list()
    app.contact.add_new_user(user)
    assert len(old_user_list) + 1 == app.contact.count()
    new_user_list = app.contact.get_user_list()
    old_user_list.append(user)
    assert sorted(old_user_list, key=Contact.id_or_max) == sorted(new_user_list, key=Contact.id_or_max)

