import profile
from django.db import models
#from django.db.models.fields import IntegerField
class StudentModel(models.Model):
    name=models.CharField(max_length=200)
    classs=models.IntegerField()
    rollnumber=models.IntegerField()

class clasModel(models.Model):
    clas=models.OneToOneField(StudentModel,on_delete=models.CASCADE)
    school=models.CharField(max_length=400)

class ProfileModel(models.Model):
    profile=models.OneToOneField(StudentModel,on_delete=models.CASCADE)
    fathername=models.CharField(max_length=200)
    mothername=models.CharField(max_length=200)
    address=models.CharField (max_length=500)
    emailid=models.EmailField()
    contactnumber=models.IntegerField()
    image=models.URLField()
   # image1=models.URLField()
   # image2=models.URLField()
   # image3 = models.URLField()
    
class Images(models.Model):
    Image_detail=models.OneToOneField(StudentModel,on_delete=models.CASCADE)
    image=models.ImageField()
    image1=models.ImageField()
    image2=models.ImageField()
    image3=models.ImageField()



    