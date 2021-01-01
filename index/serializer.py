'''
创建 序列化器
'''

from index.models import Teacher, Student
from rest_framework import serializers

class StudentSer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class TeacherSer(serializers.ModelSerializer):
    # 显示所属组的名称
    # permission = serializers.ReadOnlyField(source='permission.username')
    class Meta:
        model = Teacher
        fields = '__all__'
