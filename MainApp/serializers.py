from django.contrib.auth.models import User,Group
from rest_framework import serializers
from MainApp.models import Course, Department
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'url', 'email', 'groups')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('name','url')

class CourseSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True,allow_blank=False,max_length=100)
    desc = serializers.CharField(required=True)
    department = serializers.PrimaryKeyRelatedField(queryset=Department.objects.all())
    created = serializers.DateTimeField()
    def create(self, validated_data):
        return Course.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.desc = validated_data.get('desc',instance.desc)
        instance.department = validated_data.get('department',instance.department)
        instance.save()
        return instance

class DepartmentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    created = serializers.DateTimeField()
    def create(self, validated_data):
        return Department.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.save()
        return instance 

class AttendanceSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    student_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.filter(groups__name='students'))
    teacher_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.filter(groups__name='teachers'))
    date = serializers.DateTimeField()
    present = serializers.BooleanField(default=False)
    
