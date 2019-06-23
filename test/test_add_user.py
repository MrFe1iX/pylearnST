# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_user(app):
    old_user_list = app.contact.get_user_list()
    app.contact.add_new_user(Contact(firstname="Test", middlename="OlO",
                                     lastname="Testovich", nick="tes", email="test@test.ru",
                                     address="Moskovskaz 12", month=2, day="10", year="1984"))
    new_user_list = app.contact.get_user_list()
    assert len(old_user_list) + 1 == len(new_user_list)

