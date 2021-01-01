'''
创建 视图聚合
'''
from index.serializer import StudentSer, TeacherSer
from index.models import Student, Teacher
from rest_framework import viewsets, permissions

class StuViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSer
    permission_classes = (permissions.IsAuthenticated,)

class TeaViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSer
    permission_classes = (permissions.IsAuthenticated,)
