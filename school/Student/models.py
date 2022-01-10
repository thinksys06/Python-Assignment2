from django.db import models
#from django.db.models.fields import IntegerField
class StudentModel(models.Model):
    name=models.CharField(max_length=200)
    classs=models.IntegerField()
    rollnumber=models.IntegerField()

class clasModel(models.Model):
    clas=models.OneToOneField(StudentModel,on_delete=models.CASCADE)
    school=models.CharField(max_length=400)
