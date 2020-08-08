# python

 Python supports both functional and object-oriented programming language

Object-oriented programming based on the main features that are: 
1. Abstraction: It helps in letting the useful information or relevant data to a user, which increases the efficiency of the program and make the things simple.
2. Inheritance: It helps in inheriting the methods, functions, properties, and fields of a base class in the derived class. 
3. Polymorphism: It helps in doing one task in many ways with the help of overloading and overriding which is also known as compile-time and run-time polymorphism respectively. 
4. Encapsulation: It helps in hiding the irrelevant data from a user and prevents the user from unauthorized access.

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


Functional programming is a technique that emphasizes the evaluation of functions. It gets its name from writing functions that provide the main source of logic in a program. The concept behind functional programming is for the functions to be stateless and rely only on the given inputs to produce an output. Functional programming is a paradigm that treats computation as the evaluation of mathematical functions and avoids changing states and mutable data. It is based on different concepts, including pure functions, recursion, high order functions, type systems, and referential transparency.

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
