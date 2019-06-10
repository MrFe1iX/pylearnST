# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_user(app):
    app.session.login(username="admin", password="secret")
    app.contact.add_user_info(Contact(firstname="Test", middlename="OlO",
                                lastname="Testovich", nick="tes", email="test@test.ru",
                                address="Moskovskaz 12", month=2, day="10", year="1984"))
    app.session.logout()

