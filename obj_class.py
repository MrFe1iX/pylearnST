
class Group:

    def __init__(self, name, header, footer):
        self.name = name
        self.header = header
        self.footer = footer


class User:

    def __init__(self, firstname, middlename, lastname, nick,
                 email, address, month, day, year):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nick = nick
        self.email = email
        self.address = address
        self.month = month
        self.day = day
        self.year = year
