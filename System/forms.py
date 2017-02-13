import datetime
from django import forms
from .models import Patient, Physician, Appointment
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm

class AppointmentForm(forms.Form):
    doctor_name = forms.CharField(required=True)
    date = forms.CharField(required=True)
    description = forms.CharField(widget=forms.Textarea(attrs={'rows': 5}))
    hospital_choices = (('Bob Ross  Hospital', 'Bob Ross Hospital'),('Moms Spaghetti Hospital', 'Moms Spaghetti Hospital'))
    hospital = forms.CharField(required=True, widget=forms.widgets.Select(choices=hospital_choices))
#############################################
#-------------Appointment Form--------------#
# Imports the data from the appregister     #
# HTML template and creates an appointment  #
# object.                                   #
#############################################
class AppointmentForm(forms.ModelForm):

    # todo change the field types
    # patient_username = forms.CharField(widget=forms.widgets.Select())
    doctor_name = forms.CharField(required=True)
    date = forms.CharField(required=True)
    time = forms.CharField(required=True)
    description = forms.CharField(required=True)
    hospital = forms.CharField(required=True)

    #date = forms.CharField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    #time = forms.CharField(widget=forms.widgets.TimeInput(attrs={'type': 'time'}))


    class Meta:
        model = Appointment
        fields = ('doctor_name', 'date', 'time', 'description', 'hospital')

    def get_appointment(self, commit = True):

        # save the form
        app = super(AppointmentForm, self).save(commit=False)
        app.doctor_name = self.cleaned_data['doctor_name']
        app.date = self.cleaned_data['date']
        app.time = self.cleaned_data['time']
        app.description = self.cleaned_data['description']
        app.hospital = self.cleaned_data['hospital']

#############################################



#############################################
#--------Patient Registration Form----------#
# Imports the data from the registration    #
# HTML template and creates a patient       #
# object.                                   #
#############################################

class PatientRegister(forms.ModelForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.CharField(required=True)
    sex = forms.CharField(required=True)
    phone_number = forms.CharField(required=True)
    address = forms.CharField(required=True)
    city = forms.CharField(required=True)
    state = forms.CharField(required=True)
    zipcode = forms.IntegerField(required=True,min_value=10000)
    health_insurance_number = forms.IntegerField(required=True,min_value=1000)
    password = forms.CharField(widget=forms.TextInput(attrs={'type': 'password'}))
    # hospital_choices = (('Bob Ross  Hospital', 'Bob Ross Hospital'),('Moms Spaghetti Hospital', 'Moms Spaghetti Hospital'))
    # hospital = forms.CharField(required=True, widget=forms.widgets.Select(choices=hospital_choices))

    class Meta:
        model = User
        fields = ('username', 'password','email')

    def save(self, commit=True):
        user = super(PatientRegister, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            g, created = Group.objects.get_or_create(name="Patient")
            g.user_set.add(user)
            patient = Patient.objects.create(user=user)
            patient.first_name = self.cleaned_data['first_name']
            patient.last_name = self.cleaned_data['last_name']
            patient.email = self.cleaned_data['email']
            patient.phone_number = self.cleaned_data['phone_number']
            patient.sex = self.cleaned_data['sex']
            patient.address = self.cleaned_data['address']
            patient.city = self.cleaned_data['city']
            patient.state = self.cleaned_data['state']
            patient.zipcode = self.cleaned_data['zipcode']
            patient.health_insurance_number = self.cleaned_data['health_insurance_number']
            patient.save()
        return user
#############################################



#############################################
#--------Generic Registration Form----------#
#############################################
class UserRegister(forms.ModelForm):

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "password"]
#############################################



#############################################
#-----------Patient Update Form-------------#
# Imports the data from the proedit HTML    #
# template and updates the current user's   #
# profile information with it               #
#############################################
class UpdatePatient(forms.ModelForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    phone_number = forms.CharField(required=True)
    address = forms.CharField(required=True)
    city = forms.CharField(required=True)
    state = forms.CharField(required=True)
    zipcode = forms.IntegerField(required=True,min_value=10000)
    health_insurance_number = forms.IntegerField(required=True,min_value=1000)
    #hospital_choices = (('Bob Ross  Hospital', 'Bob Ross Hospital'),('Moms Spaghetti Hospital', 'Moms Spaghetti Hospital'))
    #hospital = forms.CharField(required=True, widget=forms.widgets.Select(choices=hospital_choices))

    class Meta:
        model = Patient
        fields = ('first_name', 'last_name', 'phone_number', 'address', 'city', 'state', 'zipcode', 'health_insurance_number')
#############################################