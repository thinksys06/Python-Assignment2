#from .views import StudentView,clasView,ProfileView#ImageView
from .views import DocView, StudentView,clasView,ProfileView,ImageView,DocView,galleryView,likeview,dislikeview,Student_View
from rest_framework import routers, urlpatterns
from django.urls import path,include
router=routers.DefaultRouter()
router.register('student',StudentView)
router.register('class',clasView)
router.register('profile',ProfileView)
router.register('image',ImageView)
router.register('Doc',DocView)
router.register('gallery',galleryView)
router.register('like',likeview)
router.register('dislike',dislikeview)
urlpatterns=[
    path('views/',Student_View),
    path('api/',include(router.urls))
]
