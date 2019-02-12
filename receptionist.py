from employee import Employee
from record import Record

class Receptionist(Employee):
	# def __init__(self, name, staff_id, authorization_code):
	# 	super().__init__(name, staff_id)
	# 	self.authorization_code = 1

	def view_patient_record(self, patient_id):
		return print(patient_id)