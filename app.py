from patient import Patient
from doctor import Doctor
from janitor import Janitor

'''
Patient object test
'''
patient1 = Patient("Patient 1", 123456)
# print(patient1)

'''
Doctor object test
'''
doctor1 = Doctor('Doctor 1', 1001, 1)
# doctor1.view_patient_record(patient1)
doctor1.add_patient_record(patient_id=patient1, title="Dehydration", description="Lack of water")
doctor1.add_patient_record(patient1, "Migraine", description="Lack of sleep")
doctor1.view_patient_record(patient1)
doctor1.report_status(title="Clock in", description="Time to work at 8am")
doctor1.report_status(title="Clock out", description="Time to work at 5pm")
doctor1.view_self_record()

'''
Janitor object test
'''
janitor1 = Janitor('Janitor 1', 2001, 2)
janitor1.report_status(title="Clock in", description="Time to work at 8am")
janitor1.report_status(title="Clock out", description="Time to work at 5pm")
# janitor1.view_self_record()