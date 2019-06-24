# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    old_group = app.group.get_group_list()
    group = Group(name="Testing", header="OLOLOLOLOLO", footer="SUPER CLASS")
    app.group.create(group)
    new_group = app.group.get_group_list()
    assert len(old_group) + 1 == len(new_group)
    old_group.append(group)
    assert sorted(old_group, key=Group.id_or_max) == sorted(new_group, key=Group.id_or_max)


def test_none_group(app):
    old_group = app.group.get_group_list()
    group = Group(name="", header="", footer="")
    app.group.create(group)
    new_group = app.group.get_group_list()
    assert len(old_group) + 1 == len(new_group)
    old_group.append(group)
    assert sorted(old_group, key=Group.id_or_max) == sorted(new_group, key=Group.id_or_max)