from patient import Patient
from doctor import Doctor
from janitor import Janitor
from employee import Employee
from admin import Admin
from receptionist import Receptionist

from collections import OrderedDict
import sys, os

'''
Patient object test
'''
patient1 = Patient("Patient 1", 123456)
# print(patient1)

'''
Doctor object test
'''
doctor1 = Doctor('Doctor 1', 3000, 3)
# doctor1.view_patient_record(patient1)
doctor1.add_patient_record(patient_id=patient1, title="Dehydration", description="Lack of water")
doctor1.add_patient_record(patient1, "Migraine", description="Lack of sleep")
# doctor1.view_patient_record(patient1)
doctor1.report_status(title="Clock in", description="Time to work at 8am")
doctor1.report_status(title="Clock out", description="Time to work at 5pm")
# doctor1.view_self_record()
# doctor1.list_patients()

'''
Janitor object test
'''
janitor1 = Janitor('Janitor 1', 1000, 1)
# janitor1.report_status(title="Clock in", description="Time to work at 8am")
# janitor1.report_status(title="Clock out", description="Time to work at 5pm")
# janitor1.view_self_record()

'''
Receptionist object test
'''
receptionist1 = Receptionist('Receptionist 1', 2000, 2)

'''
Admin object test
'''
admin1 = Admin('Admin1', 4000, 4)

def clear():
	os.system('cls' if os.name =='nt' else 'clear')

def menu_loop():
	'''Show the menu'''
	login_user = None
	username = input("Please enter your username: ")
	for employee in Employee.employee_list:
		if username == employee.name:
			login_user = employee
	# print(login_user.staff_id)
	password = int(input("Please enter your password: "))
	if login_user.staff_id == password:
		clear()
		print(f"Welcome {login_user.name}")
	else:
		print("Wrong password or username, please try again.")

	if login_user.authorization_code > 1:
		menu.update({'w': view_patient_record})
	if login_user.authorization_code > 2:
		menu.update({'a': add_patient_record})
		menu.update({'s': remove_patient_record})
		menu.update({'d': list_patients})
	if login_user.authorization_code > 3:
		menu.update({'z': view_employee_record})
		menu.update({'x': add_employee_record})
		menu.update({'c': remove_employee_record})
		menu.update({'v': list_employees})

	choice = None
	while choice != 'q':
		print("Enter 'q' to quit.")
		for key, value in menu.items():
			print(f'{key}) {value}')
		choice = input('Action: ').lower().strip()

		if choice in menu:
			clear()
			menu[choice]()

def view_patient_record(login_user):
	patient_id = int(input("Enter the Patient ID to search: "))
	login_user.view_patient_record(patient_id)

def add_patient_record(login_user):
	patient_id = int(input("Enter the Patient ID to search: "))
	record_title = input("What will be the title of record: ")
	record_description = input("What will be the description of record: ")
	login_user.add_patient_record(patient_id, record_title, record_description)

def remove_patient_record(login_user):
	patient_id = int(input("Enter the Patient ID to search: "))
	record_id = int(input("What will be the index of record to be removed: "))
	login_user.delete_patient_record(patient_id, record_id)

def list_patients(login_user):
	login_user.list_patients()

def view_employee_record(login_user):
	employee_id = int(input("Enter the Employee ID to search: "))
	login_user.view_employee_record(employee_id)

def add_employee_record(login_user):
	employee_id = int(input("Enter the Employee ID to search: "))
	record_title = input("What will be the title of record: ")
	record_description = input("What will be the description of record: ")
	login_user.add_employee_record(employee_id, record_title, record_description)

def remove_employee_record(login_user):
	employee_id = int(input("Enter the Employee ID to search: "))
	record_id = int(input("What will be the index of record to be removed: "))
	login_user.delete_employee_record(employee_id, record_id)

def list_employees(login_user):
	login_user.list_employees()

menu = OrderedDict([
	# ('v', view_record),
	# ('a', add_record),
	# ('r', remove_record),
	# ('l', list_record),
])

if __name__ == '__main__':
	menu_loop()