from __future__ import unicode_literals
from django.db import models

# Create your models here.

START_YEAR = 2017
FEBURARY_DAY = 28
ODD_DAY = 31
EVEN_DAY = 30

class Day:
	def __init__(self, day, coin = "BITCOIN", subject = "",important = False):
		self.day = day
		self.subject = subject
		self.important = important
		self.event = False
		self.coin = coin

class Month:
	def __init__(self, month, total_days):
		self.month = month
		self.total_days = total_days
		self.day = {}
		self.coin_var = set([])
		self.event_count = 0
		for i in range(1, self.total_days + 1):
			self.day[i] = Day(i)

	def print_all_event(self):
		string, temp = "", ""
		self.event_count = 0
		for i in range(1, self.total_days + 1):
			if self.day[i].event:
				self.event_count += 1
				temp += ("   " + str(self.day[i].day) + " : " + str(self.day[i].subject) + " \n")
		string += (str(self.month) + "'s event list : \n" + "  < total event : " + str(self.event_count) + " > \n")
		string += temp
		return string

class Calendar:
	def __init__(self, year):
		self.year = year
		self.month = {}
		self.create_month()

	def trans_name(self, inp):
		"""
		number of month -> name of month / name of month -> number of month
		"""
		if inp == 1:
			return "January"
		elif inp == 2:
			return "Feburary"
		elif inp == 3:
			return "March"
		elif inp == 4:
			return "April"
		elif inp == 5:
			return "May"
		elif inp == 6:
			return "June"
		elif inp == 7:
			return "July"
		elif inp == 8:
			return "August"
		elif inp == 9:
			return "September"
		elif inp == 10:
			return "October"
		elif inp == 11:
			return "November"
		elif inp == 12:
			return "December"
		elif inp == "January":
			return 1
		elif inp == "Feburary":
			return 2
		elif inp == "March":
			return 3
		elif inp == "April":
			return 4
		elif inp == "May":
			return 5
		elif inp == "June":
			return 6
		elif inp == "July":
			return 7
		elif inp == "August":
			return 8
		elif inp == "September":
			return 9
		elif inp == "October":
			return 10
		elif inp == "November":
			return 11
		elif inp == "December":
			return 12

	def create_month(self):
		for i in range(1, 13):
			month_name = self.trans_name(i)
			if i == 2:
				self.month[month_name] = Month(month_name, FEBURARY_DAY)
				# print self.year, self.month[month_name].month, self.month[month_name].print_all_event()
			elif i % 2 == 0:
				self.month[month_name] = Month(month_name, EVEN_DAY)
				# print self.year, self.month[month_name].month, self.month[month_name].print_all_event()
			else:
				self.month[month_name] = Month(month_name, ODD_DAY)
				# print self.year, self.month[month_name].month, self.month[month_name].print_all_event()


	def fill(self, month, day, coin, subject):
		if type(month) == type(1):
			month = self.trans_name(month)
		temp_month = self.month[month]
		temp_day = temp_month.day[day]
		
		temp_month.event_count += 1
		temp_day.subject = subject
		temp_day.event = True
		

data = {}
for i in range(START_YEAR, START_YEAR + 4):
	data[i] = Calendar(i)


def test():
	"""
	for test
	"""
	print data[2017].month.items()
	for i in range(1, 20):
		print data[2017].month["Feburary"].day[i].day
	data[2017].fill("Feburary",25,"BITCOIN"," first memo")
	print data[2017].month["Feburary"].print_all_event()
