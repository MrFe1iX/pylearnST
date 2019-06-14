# -*- coding: utf-8 -*-
from model.contact import Contact


def test_edit_first_user(app):
    app.contact.edit_user_info(Contact(firstname="New", middlename="Maxim", lastname="Speders",
                                       nick="Nos", email="ylika@mail.cru", address="Josedr sa 21",
                                       month=6, day="12", year="1966"))


def test_edit_firstname(app):
    app.contact.edit_user_info(Contact(firstname="Oloha"))


def test_edit_middlename(app):
    app.contact.edit_user_info(Contact(middlename="Oloha+++OKs"))


def test_edit_email(app):
    app.contact.edit_user_info(Contact(email="Oloha@mmmmmmail.ru"))
