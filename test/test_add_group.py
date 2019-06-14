# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.group.create(Group(name="Testing", header="OLOLOLOLOLO", footer="SUPER CLASS"))


def test_none_group(app):
    app.group.create(Group(name="", header="", footer=""))

