from django.shortcuts import render,redirect
from rest_framework.viewsets import ModelViewSet
from .models import StudentModel,clasModel,ProfileModel,Images,Doc, gallery,likes,dislike
from .serializer import StudentSerializer,clasSerializer,ProfileSerializer,ImageSerial,DocSerial,gallerySerial,likesSerial,dislikeSerial

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

class DocView(ModelViewSet):
    serializer_class=DocSerial
    queryset=Doc.objects.all()

class galleryView(ModelViewSet):
    serializer_class=gallerySerial
    queryset=gallery.objects.all()
def addPhoto(request):
    if request.method == 'POST':
        data = request.POST
        images = request.FILES.getlist('images')
        for image in images:
                image=image,
            

        return redirect('index')

class likeview(ModelViewSet):
    serializer_class=likesSerial
    queryset=likes.objects.all()

class dislikeview(ModelViewSet):
    serializer_class=dislikeSerial
    queryset=dislike.objects.all()

def Student_View(request):
    student = StudentModel.objects.all()
    context={'student':student}
    return render(request,'index.html',context)
