import profile
from django.db import models
#from django.db.models.fields import IntegerField
class StudentModel(models.Model):
    name=models.CharField(max_length=200)
    classs=models.IntegerField()
    rollnumber=models.IntegerField()
    image=models.ImageField(default="bear-grylls.jpg", null=True, blank=True)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

class clasModel(models.Model):
    clas=models.OneToOneField(StudentModel,on_delete=models.CASCADE)
    school=models.CharField(max_length=400)

class ProfileModel(models.Model):
    profile=models.OneToOneField(StudentModel,on_delete=models.CASCADE)
    fathername=models.CharField(max_length=200)
    mothername=models.CharField(max_length=200)
    #gender=models.CharField(max_length=50)
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

class Doc(models.Model):
    Doc_detail=models.ForeignKey(StudentModel,on_delete=models.CASCADE)
    Doc=models.ImageField()
    Doc=models.ImageField()
    Doc=models.ImageField()
    Doc=models.ImageField()

class gallery(models.Model):
    galerry_detail=models.ForeignKey(StudentModel,on_delete=models.CASCADE)
    Pic=models.URLField()

class likes(models.Model):
    like=models.ManyToManyField(StudentModel)
    Like=models.BooleanField()
class dislike(models.Model):
    dislike=models.ManyToManyField(StudentModel)
    Dislike=models.BooleanField()




    