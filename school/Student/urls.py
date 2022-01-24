#from .views import StudentView,clasView,ProfileView#ImageView
from .views import StudentView,clasView,ProfileView,ImageView
from rest_framework import routers, urlpatterns
from django.urls import path,include
router=routers.DefaultRouter()
router.register('student',StudentView)
router.register('class',clasView)
router.register('profile',ProfileView)
router.register('image',ImageView)
urlpatterns=[
    path('api/',include(router.urls))
]
