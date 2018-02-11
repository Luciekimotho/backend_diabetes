from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Profile, Doctor, Caregiver, Reading, Reminder
from .serializers import UserSerializer, ProfileSerializer, ReadingSerializer, UserInlineSerializer, DoctorSerializer, CaregiverSerializer, ReminderSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.parsers import JSONParser
from rest_framework import generics
from rest_framework.decorators import api_view
from django.utils import timezone
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_201_CREATED, HTTP_202_ACCEPTED

# Create your views here.
from django.http import HttpResponse

def index(request):
    return render(request, 'diabetes/index.html')

class UserList(generics.ListCreateAPIView):
    paginator=None
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ProfileList(generics.ListCreateAPIView):
    paginator=None
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    

class ProfileDetail(APIView):
    def get_object(self, pk):
            return Profile.objects.get(pk=pk)
        
    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = ProfileSerializer(user)
        return Response(serializer.data)


class ReadingsList(generics.ListCreateAPIView):
    paginator=None
    queryset = Reading.objects.all()
    serializer_class = ReadingSerializer

class Readings(generics.ListCreateAPIView):
    paginator=None
    users = User.objects.all()
    queryset = Reading.objects.filter(user__in = users)
    serializer_class = ReadingSerializer

class ReadingDetail(APIView):
    def get_object(self, pk):
            return Reading.objects.get(pk=pk)
               
    def get(self, request, pk, format=None):
        reading = self.get_object(pk)
        readingSerializer = ReadingSerializer(reading)
        return Response(readingSerializer.data)

class UserReadingList(generics.ListCreateAPIView):
    queryset = Reading.objects.all()
    serializer_class = ReadingSerializer

class UserReading(APIView):
    def get_object(self, pk):
         return Profile.objects.get(pk=pk)

    def get(self, request, pk, format=None):
        glucoseLevel = self.get_object(pk)
        userreadingSerializer = UserInlineSerializer(glucoseLevel)
        return Response(userreadingSerializer.data)

class DoctorList(generics.ListCreateAPIView):
    paginator=None
    queryset = Reminder.objects.all()
    serializer_class = DoctorSerializer
    

class DoctorProfile(APIView):
    def get_object(self, pk):
         return Doctor.objects.get(pk=pk)

    def get(self, request, pk, format=None):
        doctor = self.get_object(pk)
        doctorSerializer = DoctorSerializer(doctor)
        return Response(doctorSerializer.data)

class CaregiverListAPIView(generics.ListCreateAPIView):
    paginator=None
    queryset = Reminder.objects.all()
    serializer_class = CaregiverSerializer

class CaregiverProfile(APIView):
    def get_object(self, pk):
         return Caregiver.objects.get(pk=pk)

    def get(self, request, pk, format=None):
        caregiver = self.get_object(pk)
        caregiverSerializer = CaregiverSerializer(caregiver)
        return Response(caregiverSerializer.data)


class ReminderListAPIView(generics.ListCreateAPIView):
    paginator=None
    queryset = Reminder.objects.all()
    serializer_class = ReminderSerializer
    # permission_classes = (IsAuthenticated,)
    # authentication_classes = (TokenAuthentication,)

def reminder_list(request):
        reminders =	Reminder.objects.filter(user=request.user)
        return render(request, 'diabetes/reminders.html', {'reminders' : reminders})

def doctor_list(request):
        doctors =	Doctor.objects.all
        return render(request, 'diabetes/doctors.html', {'doctors' : doctors})

def caregiver_list(request):
        caregiver =	Caregiver.objects.all
        return render(request, 'diabetes/caregivers.html', {'caregiver' : caregiver})

def reading_list(request):
        readings =	Reading.objects.filter(user=request.user)
        return render(request, 'diabetes/readings.html', {'readings' : readings})

def patient_list(request):
        patients =	Profile.objects.all
        return render(request, 'diabetes/patients.html', {'patients' : patients})
  
    # def get(self, request):
    #     reminderlist = Reminder.objects.all()
    #     reminderSerializer = ReminderSerializer(reminderlist,many=True)
    #     return Response(reminderSerializer.data)

    # def post(self, request):
    #     data = JSONParser().parse(request)
    #     serializer = ReminderSerializer(data=data)
    #     if serializer.is_valid():
    #         serializer.save()   
    #         return JsonResponse(serializer.data, status=201)
    #     return JsonResponse(serializer.errors, status=400)

class ReadingCreateView(generics.CreateAPIView):
    serializer_class = ReadingSerializer

    @api_view(["POST"])
    def new_reading(request):
        serializer = ReadingSerializer(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "New reading"}) 
        else:
            data = {
            "error": True,
            "errors": serializer.errors,          
            }
            return Response(data)

class ReminderCreateView(generics.CreateAPIView):
    serializer_class = ReminderSerializer

    @api_view(["POST"])
    def new_reading(request):
        serializer = ReminderSerializer(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "New reminder"}) 
        else:
            data = {
            "error": True,
            "errors": serializer.errors,          
            }
            return Response(data)

class CaregiverCreateView(generics.CreateAPIView):
    serializer_class = CaregiverSerializer

    @api_view(["POST"])
    def new_reading(request):
        serializer = CaregiverSerializer(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "New caregiver"}) 
        else:
            data = {
            "error": True,
            "errors": serializer.errors,          
            }
            return Response(data)

