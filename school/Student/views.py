from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import StudentModel,clasModel,ProfileModel,Images
from .serializer import StudentSerializer,clasSerializer,ProfileSerializer,ImageSerial

class StudentView(ModelViewSet):
    serializer_class=StudentSerializer
    queryset=StudentModel.objects.all()
class clasView(ModelViewSet):
    serializer_class=clasSerializer
    queryset=clasModel.objects.all()
class ProfileView(ModelViewSet):
    serializer_class=ProfileSerializer
    queryset=ProfileModel.objects.all()
class ImageView(ModelViewSet):
    serializer_class=ImageSerial
    queryset=Images.objects.all()