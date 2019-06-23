class Contact:

    def __init__(self, firstname=None, middlename=None, lastname=None, nick=None,
                 email=None, address=None, month=None, day=None, year=None, id=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nick = nick
        self.email = email
        self.address = address
        self.month = month
        self.day = day
        self.year = year
        self.id = id

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.firstname, self.lastname)

    def __eq__(self, other):
        return self.id == other.id and self.firstname == other.firstname and self.lastname == other.lastname

