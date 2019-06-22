# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    old_group = app.group.get_group_list()
    app.group.create(Group(name="Testing", header="OLOLOLOLOLO", footer="SUPER CLASS"))
    new_group = app.group.get_group_list()
    assert len(old_group) + 1 == len(new_group)


def test_none_group(app):
    old_group = app.group.get_group_list()
    app.group.create(Group(name="", header="", footer=""))
    new_group = app.group.get_group_list()
    assert len(old_group) + 1 == len(new_group)
