# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
from model.contact import Contact


def test_del_first_user(app):
    if app.contact.count() == 0:
        app.contact.add_new_user(Contact(firstname="111", middlename="111", lastname="111",
                                       nick="11", email="ylika@mail.cru", address="aJocxvvxcsedr s 21",
                                       month=6, day="11", year="1998"))
    app.contact.del_first_user()


def test_del_all_user(app):
    while app.contact.count() < 2:
        app.contact.add_new_user(Contact(firstname="111", middlename="111", lastname="111",
                                       nick="11", email="ylika@mail.cru", address="aJocxvvxcsedr s 21",
                                       month=6, day="11", year="1998"))
    app.contact.del_all_user()

