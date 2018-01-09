import json

class Account(object):
	num_accounts = 0

	def __init__(self, name, balance):
		self.name = name
		self.balance = balance
		Account.num_accounts += 1

	def del_account(self):
		Account.num_account -= 1

	def deposit(self, amt):
		self.balance += amt

	def withdraw(self, amt):
		self.balance -= amt

	def inquiry(self):
		return "Name={}, balance={}".format(self.name, self.balance)

	@classmethod
	def from_json(cls, params_json):
		params = json.loads(params_json)
		return cls(params.get("name"), params.get("balance"))

	def __getattr__(self, name):
		return "No attribute {}".format(name)

class CustomList(object):
	def __init__(self, container=None):
		if container is None:
			self.container = []
		else:
			self.container = container

	def __len__(self):
		return len(self.container)

	def __getitem__(self, index):
		return self.container[index]

	def __setitem__(self, index, value):
		if index <= len(self.container):	
			self.container[index] = value
		else:
			return IndexError()

	def __contains__(self, value):
		return value in self.container

	def __repr__(self):
		return str(self.container)

	def __add__(self, otherList):
		return CustomList(self.container + otherList.container)
		
		
