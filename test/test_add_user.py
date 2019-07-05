# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import string
import random


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def rand_dig(maxlen):
    dig = string.digits
    return "".join([random.choice(dig) for i in range(random.randrange(maxlen))])


user_data = [Contact(firstname=random_string("firstname", 10), middlename=random_string("middlename", 10), lastname=random_string("lastname", 10),
                     nick=random_string("nick", 10), email1="test@test.ru", address=random_string("address", 10), homephone=rand_dig(10),
                     mobilephone=rand_dig(10), workphone=rand_dig(10), fax=rand_dig(10), month=2,
                     day="10", year="1984")
             for i in range(5)
             ]


@pytest.mark.parametrize("user", user_data, ids=[repr(x) for x in user_data])
def test_add_user(app, user):
    old_user_list = app.contact.get_user_list()
    app.contact.add_new_user(user)
    assert len(old_user_list) + 1 == app.contact.count()
    new_user_list = app.contact.get_user_list()
    old_user_list.append(user)
    assert sorted(old_user_list, key=Contact.id_or_max) == sorted(new_user_list, key=Contact.id_or_max)

