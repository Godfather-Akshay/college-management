from django.contrib.auth.models import User, Group
from MainApp.models import Course, Department, Attendance
from rest_framework import viewsets
from MainApp.serializers import UserSerializer, GroupSerializer, CourseSerializer, DepartmentSerializer, AttendanceSerializer
from django.http import HttpResponse

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
class StudentViewSet(viewsets.ModelViewSet):
    queryset = User.objects.filter(groups__name='students')
    serializer_class = UserSerializer
class TeacherViewSet(viewsets.ModelViewSet):
    queryset = User.objects.filter(groups__name='teachers')
    serializer_class = UserSerializer
class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
def index(req):
    return HttpResponse('Hello, World!')

