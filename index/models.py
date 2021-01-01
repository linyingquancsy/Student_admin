from django.db import models

# Create your models here.

class Student(models.Model):
    stu_id = models.IntegerField(primary_key=True)
    stu_name = models.CharField(max_length=32)
    sex = models.CharField(max_length=2)
    chinese = models.IntegerField()
    mathematics = models.IntegerField()
    English = models.IntegerField()

    def __str__(self):
        return self.stu_name

class Teacher(models.Model):
    tea_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=32)
    age = models.IntegerField()
    # 将老师与后台管理员进行绑定，后台管理员与老师是一对多关系
    # permission = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

