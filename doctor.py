from employee import Employee
from patient import Patient
from record import Record

class Doctor(Employee):
	# inherit all from employees
	# def __init__(self, name, staff_id, authorization_code):
	# 	super().__init__(name, staff_id)
	# 	self.authorization_code = 2

	def view_patient_record(self, patient_id):
		return print(patient_id.records)

	def add_patient_record(self, patient_id, title, description):
		new_record = Record(added_by=self.staff_id, title=title, description=description)
		patient_id.records.append(new_record)
		return print("Record added")

	def delete_patient_record(self, patient_id, record_id):
		patient_id.records.remove(record_id)
		return print("Record deleted")

	def list_patients(self):
		print(f"Total patients: {len(Patient.patient_list)}")
		for patient in Patient.patient_list:
			print(f"{patient.name}: {len(patient.records)} records")