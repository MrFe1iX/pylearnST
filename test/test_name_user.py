from model.contact import Contact


def test_name_user(app, db):
    if len(db.get_user_list()) == 0:
        app.contact.contact_form(
            Contact(firstname="Old", middlename="Old", lastname="jols", email1="test@gmail.com", email2="dolsc@mail.com",
                    email3="ksakdask@mail.ru", address="testssdas 21", mobilephone="21212", homephone="5723632",
                    workphone="372378782"))
    list = app.contact.get_user_list()
    for contact in list:
        assert contact.firstname == (db.get_user_list(contact.id).firstname)
        assert contact.lastname == (db.get_user_list(contact.id).lastname)
        assert contact.address == (db.get_user_list(contact.id).address)
        assert contact.all_emails_home_page == merge_emails(db.get_user_list(contact.id))
        assert contact.all_phones_home_page == merge_phones_on_home_page(db.get_user_list(contact.id))


def merge_phones_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.homephone, contact.mobilephone, contact.workphone]))))


def merge_emails(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None, [contact.email, contact.email2, contact.email3]))))


# def test_name_on_home_page(app):
#     contact = app.contact
#     contact_from_home_page = contact.get_user_list()[0]
#     contact_from_edit_page = contact.get_user_info_from_edit_page(0)
#     assert contact_from_home_page.firstname == contact_from_edit_page.firstname
#     assert contact_from_home_page.lastname == contact_from_edit_page.lastname
#
#
# def test_name_on_view_page(app):
#     contact_from_view_page = app.contact.get_user_from_view_page(0)
#     contact_from_edit_page = app.contact.get_user_info_from_edit_page(0)
#     assert contact_from_view_page.full_name == contact_from_edit_page.full_name
