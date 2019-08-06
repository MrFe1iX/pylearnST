# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
from random import randrange


def test_edit_first_user(app):
    old_user_list = app.contact.get_user_list()
    user = Contact(firstname="New", middlename="Maxim", lastname="Speders",
                                       nick="Nos", email1="ylika@mail.cru", address="Josedr sa 21",
                                       month=6, day="12", year="1966")
    user.id = old_user_list[0].id
    if app.contact.count() == 0:
        app.contact.add_new_user(Contact(firstname="111", middlename="111", lastname="111",
                                       nick="11", email1="ylika@mail.cru", address="aJocxvvxcsedr s 21",
                                       month=6, day="11", year="1998"))
    with pytest.allure.step('Редактирование информации у контакта'):
        app.contact.edit_user_info(user)
    assert len(old_user_list) == app.contact.count()
    new_user_list = app.contact.get_user_list()
    old_user_list[0] = user
    assert sorted(old_user_list, key=Contact.id_or_max) == sorted(new_user_list, key=Contact.id_or_max)


def test_edit_some_user(app):
    old_user_list = app.contact.get_user_list()
    user = Contact(firstname="New", middlename="Maxim", lastname="Speders",
                                       nick="Nos", email1="ylika@mail.cru", address="Josedr sa 21",
                                       month=6, day="12", year="1966")
    index = randrange(len(old_user_list))
    user.id = old_user_list[index].id
    if app.contact.count() == 0:
        app.contact.add_new_user(Contact(firstname="111", middlename="111", lastname="111",
                                       nick="11", email1="ylika@mail.cru", address="aJocxvvxcsedr s 21",
                                       month=6, day="11", year="1998"))
    with pytest.allure.step('Редактирование информации у случайного контакта'):
        app.contact.edit_rand_user_info(user, index)
    assert len(old_user_list) == app.contact.count()
    new_user_list = app.contact.get_user_list()
    old_user_list[index] = user
    assert sorted(old_user_list, key=Contact.id_or_max) == sorted(new_user_list, key=Contact.id_or_max)


def test_edit_firstname(app):
    if app.contact.count() == 0:
        app.contact.add_new_user(Contact(firstname="111", middlename="111", lastname="111",
                                       nick="11", email1="ylika@mail.cru", address="aJocxvvxcsedr s 21",
                                       month=6, day="11", year="1998"))
    app.contact.edit_user_info(Contact(firstname="Oloha"))


def test_edit_middlename(app):
    if app.contact.count() == 0:
        app.contact.add_new_user(Contact(firstname="111", middlename="111", lastname="111",
                                       nick="11", email1="ylika@mail.cru", address="aJocxvvxcsedr s 21",
                                       month=6, day="11", year="1998"))
    app.contact.edit_user_info(Contact(middlename="Oloha+++OKs"))


def test_edit_email(app):
    if app.contact.count() == 0:
        app.contact.add_new_user(Contact(firstname="111", middlename="111", lastname="111",
                                       nick="11", email1="ylika@mail.cru", address="aJocxvvxcsedr s 21",
                                       month=6, day="11", year="1998"))
    app.contact.edit_user_info(Contact(email1="Oloha@mmmmmmail.ru"))
