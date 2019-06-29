# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_user(app):
    old_user_list = app.contact.get_user_list()
    user = Contact(firstname="Test", middlename="OlO",
                                     lastname="Testovich", nick="tes", email="test@test.ru",
                                     address="Moskovskaz 12", homephone="9845455", mobilephone="6948484848",
                   workphone="321341221", fax="88888888",
                   month=2, day="10", year="1984")
    app.contact.add_new_user(user)
    assert len(old_user_list) + 1 == app.contact.count()
    new_user_list = app.contact.get_user_list()
    old_user_list.append(user)
    assert sorted(old_user_list, key=Contact.id_or_max) == sorted(new_user_list, key=Contact.id_or_max)

