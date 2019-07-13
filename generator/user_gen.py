# -*- coding: utf-8 -*-
from model.contact import Contact
import string
import random
import os
import jsonpickle
import getopt
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f", ["number of group", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/users.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def rand_dig(maxlen):
    dig = string.digits
    return "".join([random.choice(dig) for i in range(random.randrange(maxlen))])


testdata = [Contact(firstname=random_string("firstname", 10), middlename=random_string("middlename", 10), lastname=random_string("lastname", 10),
                     nick=random_string("nick", 10), email1="test@test.ru", address=random_string("address", 10), homephone=rand_dig(10),
                     mobilephone=rand_dig(10), workphone=rand_dig(10), fax=rand_dig(10), month=2,
                     day="10", year="1984")
             for i in range(5)
             ]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_decoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))
