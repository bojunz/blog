from django.db import models

# Create your models here.
class UserModel(models.Model):
    username = models.CharField(max_length=30,unique=True)
    password = models.CharField(max_length=16)
    email = models.EmailField()


# Create your models here.

#学院信息表
class Department(models.Model):
    d_id = models.AutoField(primary_key=True)
    d_name = models.CharField(max_length=30,unique=True)

    def __str__(self):
        return f'd_id={self.d_id},d_name={self.d_name}'

class Student(models.Model):
    s_id = models.AutoField(primary_key=True)
    s_name = models.CharField(max_length=30)
    #模式为从表连主表，dept_id为附表，被连接的Department为主表
    dept_id = models.ForeignKey('Department',on_delete=models.SET_NULL,
                                null=True) #如果一个学院没了，那么这个学生表的学院值为空

    def __str__(self):
        return f's_id={self.s_id},s_name={self.s_name},dept_id ={self.dept_id}'

class Stu_detail(models.Model):
    st_id = models.AutoField(primary_key=True)
    age = models.IntegerField()
    sex = models.BooleanField(default=1)
    intro = models.TextField(null=True)
    s_id = models.OneToOneField('Student',on_delete=models.CASCADE)

    def __str__(self):
        return f'st_id={self.st_id},st_age={self.age},sex ={self.sex},into={self.intro}'

#课程信息表
class Course(models.Model):
    c_id = models.AutoField(primary_key=True)
    c_name = models.CharField(max_length=30,unique=True)
    #多对多关系会自动创建中间表
    stu_course = models.ManyToManyField('Student')

    def __str__(self):
        return f'c_id={self.c_id},c_name={self.c_name}'
