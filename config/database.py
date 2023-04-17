import os
import peewee
from peewee import *
from dotenv import load_dotenv

load_dotenv()

HOST = os.getenv('HOST')
USER = os.getenv('USER')
PASSWORD = os.getenv('PASSWORD')
DB_NAME = os.getenv('DB_NAME')

db = MySQLDatabase(DB_NAME, host=HOST, port=3306, user=USER, password=PASSWORD)


class User(peewee.Model):
	user_id = peewee.CharField(null=False, unique=True)
	username = peewee.CharField(null=True, unique=True)
	full_name = peewee.CharField(null=True)
	balance = peewee.IntegerField()
	is_active = peewee.BooleanField(default=True)

	class Meta:
		database = db


User.create_table()
