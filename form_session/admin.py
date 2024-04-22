from django.contrib import admin

# Register your models here.

from .models import UserModel,Student,Stu_detail,Department,Course

#显示的时候自定义方法
class StudentAdmin(admin.ModelAdmin):
    #显示哪些字段
    list_display = ['s_id','s_name']
    #设置过滤
    list_filter = ['s_id']
    #设置搜索字段
    search_fields = ['s_id','s_name']
    #分页,一页显示15条数据
    list_per_page = 15

#增加或者修改的时候自定义操作
class Studetail(admin.ModelAdmin):
    #添加内容时决定显示的字段
    #fields = ['age','intro']
    fieldsets = [
        ('第一列',{'fields':['age']}),
        ('第二列',{'fields':['sex','intro']})
    ]


#对哪个模型进行修改，就在哪个模型后面进行注册
admin.site.register(UserModel)
admin.site.register(Student,StudentAdmin)
admin.site.register(Stu_detail,Studetail)
admin.site.register(Department)
admin.site.register(Course)