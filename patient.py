from datetime import datetime
from record import Record

class Patient:
	patient_list = []

	def __init__(self, name, nric, registered_date=datetime.now().strftime('%A %B %d, %Y %I:%M%p')):
		self.name = name
		self.nric = nric
		self.registered_date = registered_date
		self.records = []
		self.patient_list.append(self)

	def __repr__(self):
		if len(self.records) == 0:
			return f"{self.name} of {self.nric} has been a patient since {self.registered_date} with {len(self.records)} records so far"
		else:
			return f"{self.name} of {self.nric} has been a patient since {self.registered_date} with:\n {self.records}"