"""diabetesproj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from diabetes import views as model_views
from django.contrib.auth import views as auth_views
from rest_framework.authtoken import views as token_auth_views
# from snippets import views

urlpatterns = [
url(r'^diabetes/', include('diabetes.urls')),
url(r'^admin/', admin.site.urls),
url(r'^$', model_views.index, name='index'),

url(r'^login/$', auth_views.login, name='login'),
url(r'^logout/$', auth_views.logout, name='logout'),

url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
url(r'^api-token-auth/', token_auth_views.obtain_auth_token),
url(r'^get_auth_token/$', token_auth_views.obtain_auth_token, name='get_auth_token'),

url(r'^users/', model_views.UserList.as_view()),

url(r'^patients/', model_views.ProfileList.as_view()),
url(r'^patient/(?P<pk>[0-9]+)/$', model_views.ProfileDetail.as_view()),

url(r'^readings/', model_views.ReadingsList.as_view()),
url(r'^reading/(?P<pk>[0-9]+)/$', model_views.ReadingDetail.as_view()),
url(r'^reading/$', model_views.ReadingCreateView.as_view(), name="new_reading"),

url(r'^userreadings/', model_views.UserReadingList.as_view()),
url(r'^userreading/(?P<pk>[0-9]+)/$', model_views.UserReading.as_view()),

url(r'^reminders/', model_views.ReminderListAPIView.as_view()),
url(r'^reminder/$', model_views.ReminderCreateView.as_view(), name="new_reminder"),

url(r'^doctors/', model_views.DoctorList.as_view()),
url(r'^doctor/(?P<pk>[0-9]+)/$', model_views.DoctorProfile.as_view()),

url(r'^caregivers/', model_views.CaregiverListAPIView.as_view()),
url(r'^reminder/$', model_views.CaregiverCreateView.as_view(), name="new_caregiver"),
url(r'^caregiver/(?P<pk>[0-9]+)/$', model_views.CaregiverProfile.as_view()),


# Html rendering results
url(r'^reminderlist', model_views.reminder_list, name = 'reminder_list'),
url(r'^doctorlist', model_views.doctor_list, name = 'doctor_list'),
url(r'^patientlist', model_views.patient_list, name = 'patient_list'),
url(r'^caregiverlist', model_views.caregiver_list, name = 'caregiver_list'),
url(r'^readinglist', model_views.reading_list, name = 'reading_list'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
