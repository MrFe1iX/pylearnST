import pymysql.cursors


class DbHelper:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, name=name, user=user, password=password)

    def disconect(self):
        self.connection.close()