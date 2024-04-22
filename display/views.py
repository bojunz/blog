from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse
# Create your views here.
from .models import BlogModel
from datetime import datetime
from django.contrib.auth.models import User,Group,Permission
from django.contrib.auth import login,logout,authenticate
#视图函数权限
from django.contrib.auth.decorators import permission_required
#类视图权限
from django.utils.decorators import method_decorator
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage

def index(request):
    return render(request,'display/demo_index.html')

#添加博客
#增加权限，第一个是app名字，第二个是，加上操作名称
@permission_required('display.addblog_model')
def blog_add(request):
    #如果是get请求就是访问页面
    if request.method =='GET':
        return render(request,'display/demo_add.html')
    #如果是POST请求，那就是向页面提交数据
    elif request.method == 'POST':
        #通过HTML页面表格中的 name值 来获取填写的内容
        title = request.POST.get('title') #获取产品名
        content = request.POST.get('content') #获取产品序号
        number = request.POST.get('number') #获取产品数量
        #把数据输入数据库
        BlogModel.objects.create(name=title,sku=content,number=number)
        b_list = BlogModel.objects.all()
        return render(request,'display/demo_list.html',context={
            'b_list':b_list,
        })

#产品列表展示页面
def blog_list(request):
    b_list = BlogModel.objects.all()
    pg = Paginator(b_list,2)
    pg_range = pg.page_range
    try:
        pg_current = request.GET.get('page') #获取当前的页码
        pg_content = pg.page(pg_current)  #获取当前页面的内容
    except PageNotAnInteger:
        pg_content = pg.page(1)
    except EmptyPage:
        pg_content = pg.page(pg.num_pages)  #如果空页面，默认显示最后一页
    return render(request, 'display/demo_list.html', context={
        'pg': pg_content,
        'pg_range':pg_range
    })

#产品详情页面
def blog_detail(request,blog_id):
    blogid = BlogModel.objects.filter(sku=blog_id)
    b_list = BlogModel.objects.all()
    current_datetime = datetime.now()
    date = current_datetime.strftime('%Y/%m/%d')
    return render(request,'display/demo_detail.html',context={
        'blogid':blogid,
        'b_list': b_list,
        'date':date,
    })

def blog_delete(request,blog_id):
    blog = BlogModel.objects.filter(id=blog_id)
    if blog:
        blog.delete()
        return redirect(reverse('list'))
    else:
        return HttpResponse('产品删除失败')

def blog_update(request,blog_id):
    blog = BlogModel.objects.get(id=blog_id)
    if request.method == 'GET':
        return render(request, 'display/demo_edit.html',context={
            'blog': blog,
        })
    elif request.method == 'POST':
        #通过HTML页面表格中的 name值 来获取填写的内容
        title= request.POST.get('title') #获取产品名
        content = request.POST.get('content') #获取产品序号
        number = request.POST.get('number') #获取产品数量
        blog.name = title
        blog.sku = content
        blog.number = number

        blog.save()
        # return render(request,'display/demo_list.html',context={
        #     'blog':blog
        # })
        return redirect(reverse('list'))

#类视图
from django.views import View
class Blog_update(View): #让当前定义的类变成视图类
    def get(self,request,blog_id):
        blog = BlogModel.objects.get(id=blog_id)
        return render(request, 'display/demo_edit.html', context={
            'blog': blog,
        })

    @method_decorator(permission_required('display.change_blogmodel'))
    def post(self,request,blog_id):
        blog = BlogModel.objects.get(id=blog_id)
        title = request.POST.get('title')  # 获取产品名
        content = request.POST.get('content')  # 获取产品序号
        number = request.POST.get('number')  # 获取产品数量
        blog.name = title
        blog.sku = content
        blog.number = number

        blog.save()
        # return render(request,'display/demo_list.html',context={
        #     'blog':blog
        # })
        return redirect(reverse('list'))

def permission_add(request):
    user = User.objects.filter(username='qwe123').first() #获取要添加权限的用户
    #per = Permission.objects.filter(codename='add_blogmodel').first() #获取需要添加的权限
    per = Permission.objects.filter(codename='change_blogmodel').first() #获取需要添加的权限
    user.user_permissions.add(per) #给用户添加权限
    return HttpResponse('用户权限添加成功')

def page_test(request):
    fruit = ['桂圆','板栗','香蕉','葡萄','橘子','榴莲','西瓜','石榴','香蕉','草莓']
    #分页器,第一个是需要分页的对象，第二个是每页分多少个
    pg = Paginator(fruit,4)
    print(pg.count) #分页总共的数据
    print(pg.num_pages) #分页的总共页数
    print(pg.page_range) #分页页码的范围

    #接收页码数,里面参数代表页码数，这应该是一个类
    pg1 = pg.page(1)
    pg2 = pg.page(2)

    #属性，查看页面里面的数据
    content1 = pg1.object_list #显示第一页的数据
    print(content1)

    #方法
    pg1.has_next() #判断是否有下一页
    pg1.has_previous() #判断是否有上一页
    pg1.has_other_pages() #判断是否有上一页或者下一页

    pg1.next_page_number()  #获取下一页的页码，如果没有会报错
    pg2.previous_page_number() #获取上一页的页码，如果没有会报错

    print(pg1.start_index()) #获取当前页面第一个对象的索引，从1开始
    print(pg1.end_index()) #获取当前页面最后一个对象的索引
    print(pg2.start_index())  # 获取当前页面第一个对象的索引，从1开始
    print(pg2.end_index())  # 获取当前页面最后一个对象的索引
    return HttpResponse('查询成功')













#模型补充函数
from django.db.models import Count,Max,Min,Avg,Sum,F,Q

def model_info(request):
    #聚合查询
    res = BlogModel.objects.all().aggregate(Sum('number'))
    count = BlogModel.objects.all().aggregate(Count('sku'))
    #分组查询
    #根据dept_id分组，然后统计每个分组的dept_id的数量
    #Student.objects.values('dept_id').annotate(Count('dept_id'))

    #F查询,针对两个字段进行比较，如果相等则返回结果
    #返回s_id = dept_id的结果
    #Student.objects.filter(s_id=F('dept_id))
    #Student.objects.all().update(age=f('age')+1)

    #Q查询,and
    #Student.objects.filter(Q(name='jay') & Q(age=18))
    #Student.objects.filter(Q(name='jay') | Q(name=Tom))
    #~表示取反,名字不是jay或者名字不是Tom的
    #Student.objects.filter(~Q(name='jay') | ~Q(name=Tom))

    return render(request,'display/info.html',context={
        'res':res,
        'count':count,
    })