from employee import Employee
from record import Record

class Receptionist(Employee):
	def view_patient_record(self, patient_id):
		return print(patient_id)