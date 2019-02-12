from employee import Employee
from record import Record

class Admin(Employee):
	# inherit all from employees

	def view_patient_record(self, patient_id):
		return print(patient_id.records)

	def add_patient_record(self, patient_id, title, description):
		new_record = Record(added_by=self.staff_id, title=title, description=description)
		patient_id.records.append(new_record)
		return print("Record added")

	def delete_patient_record(self, patient_id, record_id):
		patient_id.records.remove(record_id)
		return print("Record deleted")