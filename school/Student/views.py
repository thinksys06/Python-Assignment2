from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import StudentModel,clasModel
from .serializer import StudentSerializer,clasSerializer

class StudentView(ModelViewSet):
    serializer_class=StudentSerializer
    queryset=StudentModel.objects.all()
class clasView(ModelViewSet):
    serializer_class=clasSerializer
    queryset=clasModel.objects.all()
