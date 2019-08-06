# -*- coding: utf-8 -*-
from model.group import Group
import pytest
import allure



def test_add_group(app, data_groups):
    group = data_groups
    old_group = app.group.get_group_list()
    with allure.step('Создание группы'):
        app.group.create(group)
    assert len(old_group) + 1 == app.group.count()
    new_group = app.group.get_group_list()
    old_group.append(group)
    assert sorted(old_group, key=Group.id_or_max) == sorted(new_group, key=Group.id_or_max)


def test_add_group_json(app, db, json_groups):
    group = json_groups
    old_group = db.get_group_list()
    app.group.create(group)
    assert len(old_group) + 1 == app.group.count()
    new_group = db.get_group_list()
    old_group.append(group)
    assert sorted(old_group, key=Group.id_or_max) == sorted(new_group, key=Group.id_or_max)
