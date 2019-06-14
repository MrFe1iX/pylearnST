from model.group import Group


def test_edit_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first(Group(name="EditTest", header="Edit test", footer="Edit test"))
    app.session.logout()


def test_edit_name(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first(Group(name="New name group"))
    app.session.logout()


def test_edit_header(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first(Group(header="Only header"))
    app.session.logout()


def test_edit_footer(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first(Group(footer="Only footer"))
    app.session.logout()
