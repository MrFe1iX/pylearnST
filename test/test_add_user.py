# -*- coding: utf-8 -*-
from model.contact import Contact
from fixture.application import Application
import pytest


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.death)
    return fixture


def test_add_user(app):
    app.login(username="admin", password="secret")
    app.add_user_info(Contact(firstname="Test", middlename="OlO",
                               lastname="Testovich", nick="tes", email="test@test.ru",
                               address="Moskovskaz 12", month=2, day="10", year="1984"))
    app.logout()
