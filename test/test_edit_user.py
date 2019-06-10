# -*- coding: utf-8 -*-
from model.contact import Contact


def test_edit_first_user(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_user_info(Contact(firstname="New", middlename="Maxim", lastname="Speders",
                                       nick="Nos", email="ylika@mail.cru", address="Josedr sa 21",
                                       month=6, day="12", year="1966"))
    app.session.logout()
