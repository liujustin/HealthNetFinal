"""
The models.py include all the model classes
finished models: Patient, Physicians, Appointments
"""


from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import re


#############################################
#---------------Patient class---------------#
#############################################

class Patient(models.Model):
	user = models.OneToOneField(User, related_name='patient')
	first_name = models.CharField(max_length=100,default='firstname')
	last_name = models.CharField(max_length=100, default='lastname')
	phone_number = models.IntegerField(default=0)
	address = models.CharField(max_length = 100)
	city = models.CharField(max_length = 100)
	state = models.CharField(max_length = 100)
	zipcode = models.IntegerField(default=0)
	health_insurance_number = models.IntegerField(default=0)

	def __str__(self):
		return self.first_name + " " + self.last_name

	def get_info(self):
		info = self.username + ";"
		info += self.first_name + ";"
		info += self.last_name + ";"
		info += self.password + ";"
		info += self.date_of_birth + ";"
		info += self.email + ";"
		info += self.cell_number + ";"
		info += self.address + ";"
		info += self.city + ";"
		info += self.state + ";"
		info += self.zipcode + ";"
		info += self.health_insurance_number + ";"
		info += self.hospital + ";"
		info += self.physician + ";"
		info += self.next_appointment + "\n"
		return info

	# def export_information(self):
	# 	f = open(self.name, "w")
	# 	info = self.get_info()
	# 	f.write(info)
	# 	f.close()
	# 	return self.username

	# def import_information(self):
	# 	f = open(self.name, "r")
	# 	info = f.readline()
	# 	f.close()
	# 	return info
#############################################


#############################################
#---------------Doctor class----------------#
#############################################
class Physician(models.Model):
	first_name = models.CharField(max_length=100, default='firstname')
	last_name = models.CharField(max_length=100, default='lastname')
	email = models.CharField(max_length = 100)
	work_number = models.IntegerField(default=0)
	hospital = models.CharField(max_length = 100)

	def __str__(self):
		info = "Dr. " + self.last_name
		return info

	# def export_information(self):
	# 	f = open(self.name, "w")
	# 	info = self.__str__()
	# 	f.write(info)
	# 	f.close()
	# 	return self.name

	# def import_information(self):
	# 	f = open(self.name, "r")
	# 	info = f.readline()
	# 	f.close()
	# 	return info
#############################################


class Nurse(models.Model):
	first_name = models.CharField(max_length=100, default='firstname')
last_name = models.CharField(max_length=100, default='lastname')
email = models.CharField(max_length=100)
work_number = models.IntegerField(default=0)
hospital = models.CharField(max_length=100)

#############################################
#------------Appointment class--------------#
#############################################

class Appointment(models.Model):
	# draft model TODO change date time fields appropriately
	# todo: might need to change the user field as CharField instead

	user = models.OneToOneField(User, related_name='appointment', primary_key=True)
	doctor_name = models.CharField(max_length=20, primary_key=True)
	date = models.CharField(max_length=16, primary_key=True)
	time = models.CharField(max_length=16, primary_key=True)
	description = models.CharField(max_length=200, primary_key=True)
	hospital = models.CharField(max_length=50, primary_key=True)

	# export the appointments with the username
	def export(self, username):
		return self.export_Appts(username=username)

	def export_Appts(self, username):
		appts = Appointment.objects.filter(p_username=username)
		str = ""
		for x in range(0,len(appts)):
			str += appts[x].__str__()
		str = "\n"

	# the str function of the appointment class that return the string
	# with with all the information of appointment
	def __str__(self):
		str = "{"
		str += self.doctor_name
		str += "," + self.date
		str += "," + self.time
		str += "," + self.description
		str += "," + self.hospital
		str += "}"
		return str
		#############################################