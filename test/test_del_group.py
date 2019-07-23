from model.group import Group
import random


def test_del_some_group(app, db, check_ui):
    old_group = db.get_group_list()
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="For Delete"))
    group = random.choice(old_group)
    app.group.del_group_by_id(group.id)
    assert len(old_group) - 1 == app.group.count()
    new_group = db.get_group_list()
    old_group.remove(group)
    assert old_group == new_group
    if check_ui:
        assert sorted(new_group, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)


def test_del_first_group(app):
    old_group = app.group.get_group_list()
    if app.group.count() == 0:
        app.group.create(Group(name="For Delete"))
    app.group.del_first_group()
    assert len(old_group) - 1 == app.group.count()
    new_group = app.group.get_group_list()
    old_group[0:1] = []
    assert old_group == new_group
