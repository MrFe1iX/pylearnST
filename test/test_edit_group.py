from model.group import Group


def test_edit_first_group(app):
    app.group.edit_first(Group(name="EditTest", header="Edit test", footer="Edit test"))


def test_edit_name(app):
    app.group.edit_first(Group(name="New name group"))


def test_edit_header(app):
    app.group.edit_first(Group(header="Only header"))


def test_edit_footer(app):
    app.group.edit_first(Group(footer="Only footer"))
