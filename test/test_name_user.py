

def test_name_on_home_page(app):
    contact = app.contact
    contact_from_home_page = contact.get_user_list()[0]
    contact_from_edit_page = contact.get_user_info_from_edit_page(0)
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname


def test_name_on_view_page(app):
    contact_from_view_page = app.contact.get_user_from_view_page(0)
    contact_from_edit_page = app.contact.get_user_info_from_edit_page(0)
    assert contact_from_view_page.full_name == contact_from_edit_page.full_name
