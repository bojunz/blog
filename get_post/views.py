from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    print(request)
    print(request.path)
    print(request.method)
    print(request.encoding)
    print(request.get_host())
    print(request.get_port())
    return render(request,'get_post/index.html')

def get_test(request):
    print(request.method)
    user = request.GET.get('user')
    pwd = request.GET.get('pwd')
    print(user,pwd)

    return HttpResponse('提交成功')

def get_post(request):
    print(request.method)
    user = request.POST.get('user')
    pwd = request.POST.get('pwd')
    hobby = request.POST.getlist('hobby')
    print(user,pwd,hobby)

    return HttpResponse('提交成功')

import os
from django.views import View
from blog.settings import MEDIA_ROOT
class Upload(View):

    def get(self,request):
        return render(request,'get_post/index.html')

    def post(self,request):
        #传入文件的name属性值
        f = request.FILES.get('file')
        f_name = os.path.join(MEDIA_ROOT,f.name)
        with open(f_name,'wb+') as fp:
            for i in f.chunks():  #f.chunks读取文件中的内容
                fp.write(i)
        return HttpResponse('当前文件上传完毕')

from django.http import JsonResponse
def json_test(request):
    return JsonResponse({'name':'bojun','age':18})

#设置cookie
#HttpResponse的子类
import datetime
def set_ck(request):
    response = HttpResponse('设置cookie')
    #response.set_cookie('name','admin') #如果什么都不写，代表关闭浏览器过期
    #response.set_cookie('name','admin',max_age=5) #max_age代表5秒后过期
    response.set_cookie('name','admin',expires=datetime.datetime(2024,6,1)) #指定过期时间
    return response

def get_ck(request):
    cookie = request.COOKIES
    name = cookie.get('name')
    if name =='admin':
        return HttpResponse(f'欢迎{name}登录网页')
    else:
        return HttpResponse('未登录，请先登录')

def delete_ck(request):
    response = HttpResponse('删除cookie')
    response.delete_cookie('name')
    return response