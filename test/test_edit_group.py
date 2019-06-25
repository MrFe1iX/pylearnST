from model.group import Group
from random import randrange


def test_edit_first_group(app):
    old_group = app.group.get_group_list()
    group = Group(name="EditTest", header="Edit test", footer="Edit test")
    group.id = old_group[0].id
    if app.group.count() == 0:
        app.group.create(Group(name="Lost", header="head", footer="foot"))
    app.group.edit_first(group)
    assert len(old_group) == app.group.count()
    new_group = app.group.get_group_list()
    old_group[0] = group
    assert sorted(old_group, key=Group.id_or_max) == sorted(new_group, key=Group.id_or_max)


def test_edit_some_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Lost", header="head", footer="foot"))
    old_group = app.group.get_group_list()
    group = Group(name="EditTest", header="Edit test", footer="Edit test")
    index = randrange(len(old_group))
    group.id = old_group[index].id
    app.group.edit_by_index(group, index)
    assert len(old_group) == app.group.count()
    new_group = app.group.get_group_list()
    old_group[index] = group
    assert sorted(old_group, key=Group.id_or_max) == sorted(new_group, key=Group.id_or_max)


def test_edit_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Lost"))
    app.group.edit_first(Group(name="New name group"))


def test_edit_header(app):
    if app.group.count() == 0:
        app.group.create(Group(header="head"))
    app.group.edit_first(Group(header="Only header"))


def test_edit_footer(app):
    if app.group.count() == 0:
        app.group.create(Group(footer="foot"))
    app.group.edit_first(Group(footer="Only footer"))
