from rest_framework.serializers import ModelSerializer
from .models import StudentModel,clasModel,ProfileModel
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