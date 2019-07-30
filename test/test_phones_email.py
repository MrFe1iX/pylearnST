import re
from random import randrange


def test_phones_on_home_page(app, db):
    index = randrange(len(app.contact.get_user_list()))
    contact = app.contact
    contact_from_home_page = contact.get_user_list()[index]
    contact_from_edit_page = contact.get_user_info_from_edit_page(index)
    assert contact_from_home_page.address == contact_from_edit_page.address
    assert contact_from_home_page.all_phones_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_emails_home_page == merge_emails_like_one_home_page(contact_from_edit_page)


def test_phones_on_user_view_page(app):
    contact_from_view_page = app.contact.get_user_from_view_page(0)
    contact_from_edit_page = app.contact.get_user_info_from_edit_page(0)
    assert contact_from_view_page.homephone == contact_from_edit_page.homephone
    assert contact_from_view_page.mobilephone == contact_from_edit_page.mobilephone
    assert contact_from_view_page.workphone == contact_from_edit_page.workphone


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.homephone, contact.mobilephone, contact.workphone]))))


def merge_emails_like_one_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.email1, contact.email2, contact.email3]))))