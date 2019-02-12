from record import Record

class Employee:
	employee_list = []

	def __init__(self, name, staff_id, authorization_code):
		self.name = name
		self.staff_id = staff_id
		self.authorization_code = authorization_code
		self.records = []
		self.employee_list.append(self)

	def __repr__(self):
		return f"{self.name} and {self.staff_id}"

		# clock in, clock out, take leaves etc
	def report_status(self, title, description):
		new_record = Record(title=title, description=description)
		self.records.append(new_record)

	def view_self_record(self):
		return print(f"{self.records}")