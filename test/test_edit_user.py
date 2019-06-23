# -*- coding: utf-8 -*-
from model.contact import Contact


def test_edit_first_user(app):
    old_user_list = app.contact.get_user_list()
    if app.contact.count() == 0:
        app.contact.add_new_user(Contact(firstname="111", middlename="111", lastname="111",
                                       nick="11", email="ylika@mail.cru", address="aJocxvvxcsedr s 21",
                                       month=6, day="11", year="1998"))
    app.contact.edit_user_info(Contact(firstname="New", middlename="Maxim", lastname="Speders",
                                       nick="Nos", email="ylika@mail.cru", address="Josedr sa 21",
                                       month=6, day="12", year="1966"))
    new_user_list = app.contact.get_user_list()
    assert len(old_user_list) == len(new_user_list)


def test_edit_firstname(app):
    if app.contact.count() == 0:
        app.contact.add_new_user(Contact(firstname="111", middlename="111", lastname="111",
                                       nick="11", email="ylika@mail.cru", address="aJocxvvxcsedr s 21",
                                       month=6, day="11", year="1998"))
    app.contact.edit_user_info(Contact(firstname="Oloha"))


def test_edit_middlename(app):
    if app.contact.count() == 0:
        app.contact.add_new_user(Contact(firstname="111", middlename="111", lastname="111",
                                       nick="11", email="ylika@mail.cru", address="aJocxvvxcsedr s 21",
                                       month=6, day="11", year="1998"))
    app.contact.edit_user_info(Contact(middlename="Oloha+++OKs"))


def test_edit_email(app):
    if app.contact.count() == 0:
        app.contact.add_new_user(Contact(firstname="111", middlename="111", lastname="111",
                                       nick="11", email="ylika@mail.cru", address="aJocxvvxcsedr s 21",
                                       month=6, day="11", year="1998"))
    app.contact.edit_user_info(Contact(email="Oloha@mmmmmmail.ru"))
