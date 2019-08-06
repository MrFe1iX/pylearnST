# -*- coding: utf-8 -*-
from model.group import Group
import pytest



def test_add_group(app, data_groups):
    group = data_groups
    old_group = app.group.get_group_list()
    with pytest.allure.step('Создание группы'):
        app.group.create(group)
    with pytest.allure.step('Проверка что группа +1'):
        assert len(old_group) + 1 == app.group.count()
    with pytest.allure.step('Проверка что id группы соответствует'):
        new_group = app.group.get_group_list()
        old_group.append(group)
        assert sorted(old_group, key=Group.id_or_max) == sorted(new_group, key=Group.id_or_max)


def test_add_group_json(app, db, json_groups):
    group = json_groups
    old_group = db.get_group_list()
    with pytest.allure.step('Создание группы из генератора'):
        app.group.create(group)
    with pytest.allure.step('Проверка что группа +1'):
        assert len(old_group) + 1 == app.group.count()
    with pytest.allure.step('Проверка что id группы соответствует'):
        new_group = db.get_group_list()
        old_group.append(group)
        assert sorted(old_group, key=Group.id_or_max) == sorted(new_group, key=Group.id_or_max)
