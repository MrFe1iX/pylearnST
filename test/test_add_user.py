# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest


def test_add_user(app, db, data_users):
    user = data_users
    old_user_list = db.get_user_list()
    with pytest.allure.step('Добавление контакта'):
        app.contact.add_new_user(user)
    with pytest.allure.step('Проверка что контакт +1'):
        assert len(old_user_list) + 1 == app.contact.count()
    with pytest.allure.step('Проверка что id контактов'):
        new_user_list = db.get_user_list()
        old_user_list.append(user)
        assert sorted(old_user_list, key=Contact.id_or_max) == sorted(new_user_list, key=Contact.id_or_max)


def test_add_user_json(app, db, json_users):
    user = json_users
    old_user_list = db.get_user_list()
    with pytest.allure.step('Добавление контакта из json'):
        app.contact.add_new_user(user)
    with pytest.allure.step('Проверка что контакт +1'):
        assert len(old_user_list) + 1 == app.contact.count()
    with pytest.allure.step('Проверка что id контактов'):
        new_user_list = db.get_user_list()
        old_user_list.append(user)
        assert sorted(old_user_list, key=Contact.id_or_max) == sorted(new_user_list, key=Contact.id_or_max)

