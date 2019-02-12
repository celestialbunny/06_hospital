import random

class Thief:
	def __init__(self, name, sneaky=True, **kwargs):
		self.name = name
		self.sneaky = sneaky

		for key, value in kwargs.items():
			setattr(self, key, value)

	def pickpocket(self):
		return self.sneaky and bool(random.randint(0, 1))

cc = Thief(name="cc", hobby="sleep", favorite_game="xxx")
print(cc)