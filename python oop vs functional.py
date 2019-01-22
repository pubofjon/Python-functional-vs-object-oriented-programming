#  Object oriented programming design:

import cx_Oracle as CO
class database_con(object):

  cursor = None

  def __init__(self, dsn, user, password):
    self.dsn = dsn
    self.user = user
    self.password = password

  def create_cursor(self):
    connection = CO.connect(dsn=self.dsn,
                                      user=self.user,
                                      password=self.password)
    self.cursor = connection.cursor()

  def execute(self, query, fetch):
    self.cursor.execute(query)
    if fetch == "*":
      return self.cursor.fetchall()
    return self.cursor.fetchone()

dsn=CO.makedsn('server', port_num, 'servicename')
database = Firebird(dsn=dsn, user="someuser", password="somepassword")
database.create_cursor()
result_from_query = database.execute(query="SOME QUERY", fetch="*")

# Functional programming design:

import cx_Oracle as CO

def create_cursor(dsn, user, password):
  return CO.connect(dsn=dsn, user=user, password=password).cursor()

def execute(database_cursor, query, fetch):
  database_cursor.execute(query)
  if fetch == "*":
    return database_cursor.fetchall()
  return database_cursor.fetchone()

dsn=CO.makedsn('server', port_num, 'servicename')
database_cursor = create_cursor(dsn=dsn, user="someuser", password="somepassword")
result = execute(database_cursor, fetch="*")


	