from .views import StudentView,clasView,ProfileView
from rest_framework import routers, urlpatterns
from django.urls import path,include
router=routers.DefaultRouter()
router.register('student',StudentView)
router.register('class',clasView)
router.register('profile',ProfileView)
urlpatterns=[
    path('api/',include(router.urls))
]
