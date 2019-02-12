from datetime import datetime

class Record:
	def __init__(self, title, description, added_by=None, activity_date=datetime.now().strftime('%A %B %d, %Y %I:%M%p')):
		self.title = title
		self.description = description
		self.added_by = added_by
		self.activity_date = activity_date

# doctor or receptionist addign notes should add in the "who"
	def __repr__(self):
		if self.added_by == None:
			return f"\r{self.activity_date}\n{self.title}\n{self.description}\n..."
		else:
			return f"\r{self.activity_date}\nDiagnozed by: {self.added_by}\nSickness: {self.title}\nCause: {self.description}\n..."
		# return f"{self.activity_date} - {self.description}"