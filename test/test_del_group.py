from model.group import Group


def test_del_first_group(app):
    old_group = app.group.get_group_list()
    if app.group.count() == 0:
        app.group.create(Group(name="For Delete"))
    app.group.del_first_group()
    new_group = app.group.get_group_list()
    assert len(old_group) - 1 == len(new_group)
    old_group[0:1] = []
    assert old_group == new_group


