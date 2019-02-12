from employee import Employee
from patient import Patient
from record import Record

class Admin(Employee):
	# inherit all from employees
	# def __init__(self, name, staff_id, authorization_code):
	# 	super().__init__(name, staff_id)
	# 	self.authorization_code = 3

	'''start of patient related'''
	def view_patient_record(self, patient_id):
		return print(patient_id.records)

	def add_patient_record(self, patient_id, title, description):
		new_record = Record(added_by=self.staff_id, title=title, description=description)
		patient_id.records.append(new_record)
		return print("Record added")

	def delete_patient_record(self, patient_id, record_id):
		patient_id.records.remove(record_id)
		return print("Record deleted")
	'''end of patient related'''

	'''start of employee related'''
	def view_employee_record(self, employee_id):
		return print(employee_id.records)

	def add_employee_record(self, employee_id, title, description):
		new_record = Record(added_by=self.staff_id, title=title, description=description)
		employee_id.records.append(new_record)
		return print("Record added")

	def delete_employee_record(self, employee_id, record_id):
		employee_id.records.remove(record_id)
		return print("Record deleted")
	'''end of employee related'''

	'''start of general related'''
	def list_patients(self):
		print(f"Total patients: {len(Patient.patient_list)}")
		for patient in Patient.patient_list:
			print(f"{patient.name}: {len(patient.records)} records")
			
	def list_employees(self):
		print(f"Total employees: {len(Employee.employee_list)}")
		for employee in Employee.employee_list:
			print(f"{employee.name}: {len(employee.records)} records")
	'''end of general related'''