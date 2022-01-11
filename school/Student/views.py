from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import StudentModel,clasModel,ProfileModel
from .serializer import StudentSerializer,clasSerializer,ProfileSerializer

class StudentView(ModelViewSet):
    serializer_class=StudentSerializer
    queryset=StudentModel.objects.all()
class clasView(ModelViewSet):
    serializer_class=clasSerializer
    queryset=clasModel.objects.all()
class ProfileView(ModelViewSet):
    serializer_class=ProfileSerializer
    queryset=ProfileModel.objects.all()