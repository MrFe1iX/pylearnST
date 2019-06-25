# -*- coding: utf-8 -*-
from random import randrange
from model.contact import Contact


def test_del_first_user(app):
    old_user_list = app.contact.get_user_list()
    if app.contact.count() == 0:
        app.contact.add_new_user(Contact(firstname="111", middlename="111", lastname="111",
                                       nick="11", email="ylika@mail.cru", address="aJocxvvxcsedr s 21",
                                       month=6, day="11", year="1998"))
    app.contact.del_first_user()
    assert len(old_user_list) - 1 == app.contact.count()
    new_user_list = app.contact.get_user_list()
    old_user_list[0:1] = []
    assert old_user_list == new_user_list


def test_del_some_user(app):
    if app.contact.count() == 0:
        app.contact.add_new_user(Contact(firstname="111", middlename="111", lastname="111",
                                       nick="11", email="ylika@mail.cru", address="aJocxvvxcsedr s 21",
                                       month=6, day="11", year="1998"))
    old_user_list = app.contact.get_user_list()
    index = randrange(len(old_user_list))
    app.contact.del_some_user(index)
    assert len(old_user_list) - 1 == app.contact.count()
    new_user_list = app.contact.get_user_list()
    old_user_list[index:index+1] = []
    assert old_user_list == new_user_list

# def test_del_all_user(app):
#     while app.contact.count() < 2:
#         app.contact.add_new_user(Contact(firstname="111", middlename="111", lastname="111",
#                                        nick="11", email="ylika@mail.cru", address="aJocxvvxcsedr s 21",
#                                        month=6, day="11", year="1998"))
#     app.contact.del_all_user()

