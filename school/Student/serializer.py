from rest_framework.serializers import ModelSerializer
from .models import StudentModel,clasModel
class StudentSerializer(ModelSerializer):
    class Meta:
        model=StudentModel
        fields='__all__'
class clasSerializer(ModelSerializer):
    class Meta:
        model=clasModel
        fields='__all__'