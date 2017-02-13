from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Patient, Physician, Appointment
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib import auth
from .forms import UserRegister, PatientRegister, UpdatePatient, AppointmentForm
# Create your views here.

# logger = logging.getLogger(__name__)

def index(request):
    context = {'user': request.user}
    return render(request, 'index.html', context=context)

def login_user(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
        if user:
            print("hello")
            auth.login(request, user)
            return redirect('/')
    return render(request, 'login.html')


def logout_user(request):
    # logger.info(username=request.POST.get('username') + ' has logged out')
    auth.logout(request)
    return redirect('/')

def registration(request):
    # logger.info(username=request.POST.get('username') + ' has registered')
    return render(request, 'registration.html')


# appointment registration function
def appregister(request):
    # if request.method == 'POST':
    #     form = PatientRegister(request.POST)
    #     if form.is_valid():
    #         newAppointment = form.save()
    #         newAppointment.save()
    #     else:
    #         print("error")
    # else:
    #     form = AppointmentForm()
    # return render(request, 'appregister.html', {'appreg_form': form})

    if request.method == 'POST':
        form = AppointmentForm(request.POST)

        if form.is_valid():
            newApp = form.save() # form.save return the appointment form

            newApp.save()
            return HttpResponseRedirect("/") # redirect to the index page after form being saved
        else:
            raise Http404
    else:

        form = AppointmentForm()
    return render(request, 'appregister.html', {'appreg_form': form})


def calendar(request):
    return render(request, 'calendar.html')


def profile(request):
    return render(request, 'profile.html')


def patient_home(request):
    return render(request, 'patient_home.html')


def proedit(request):
    patient = request.user.patient
    error = False

    if request.method == 'POST':
        form = UpdatePatient(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            error = True

    update_form = UpdatePatient(instance=patient)

    # logger.info(username=request.POST.get('username') + ' has updated their profile')
    context = {'update_form': update_form, 'error': error}
    return render(request, 'proedit.html', context=context)

def UserRegistration(request):
    if request.method == 'POST':
        form = PatientRegister(request.POST)
        if form.is_valid():
            newUser = form.save()
            newUser.set_password(request.POST.get('password'))
            # logger.info(username=request.POST.get('username') + ' has logged in')
            newUser.save()
        else:
            print("error")
    else:
        form = PatientRegister()

    return render(request, 'registration.html', {'u_form': form})
#############################################

