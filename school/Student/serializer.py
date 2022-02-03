from rest_framework.serializers import ModelSerializer
from .models import Images, StudentModel,clasModel,ProfileModel,Images,Doc, dislike, gallery,likes,dislike
class StudentSerializer(ModelSerializer):
    class Meta:
        model=StudentModel
        fields='__all__'
class clasSerializer(ModelSerializer):
    class Meta:
        model=clasModel
        fields='__all__'
class ProfileSerializer(ModelSerializer):
    class Meta:
        model=ProfileModel
        fields='__all__'
class ImageSerial(ModelSerializer):
    class Meta:
        model=Images
        fields='__all__'

class DocSerial(ModelSerializer):
    class Meta:
        model=Doc
        fields='__all__'

class gallerySerial(ModelSerializer):
    class Meta:
        model=gallery
        fields='__all__'

class likesSerial(ModelSerializer):
    class Meta:
        model=likes
        fields='__all__'

class dislikeSerial(ModelSerializer):
    class Meta:
        model=dislike
        fields='__all__'