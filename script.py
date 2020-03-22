from peewee import *

db = PostgresqlDatabase('trivia', user='postgres',
                        password='', host='localhost', port=5432)
