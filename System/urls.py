from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name="Index"),
    url(r'^index', views.index, name="Index"),
    url(r'^login$', views.login_user, name="Login"),
    url(r'^registration$', views.UserRegistration),
    url(r'^appregister$', views.appregister, name='AppRegister'),
    url(r'^calendar$', views.calendar, name='Calendar'),
    url(r'^profile$', views.profile, name='Profile'),
    url(r'^proedit$', views.proedit, name='Proedit'),
    url(r'^logout$', views.logout_user, name='Log out'),
    url(r'^patient_home', views.patient_home, name='Home')
    # url(r'^ts_register$', views.ts_register, name='ts_register'),
]
