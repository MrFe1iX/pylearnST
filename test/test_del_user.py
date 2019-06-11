# -*- coding: utf-8 -*-


def test_del_first_user(app):
    app.session.login(username="admin", password="secret")
    app.contact.del_edit_user()
    app.session.logout()



# def test_del_all_user(app):
#     app.session.login(username="admin", password="secret")
#     app.contact.del_all_user()
#     app.session.logout()
