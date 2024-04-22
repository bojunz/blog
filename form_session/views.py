from django.shortcuts import render,redirect,reverse
from django.views import View
from django.contrib.auth.models import User,Group,Permission
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
# Create your views here.

#下面的装饰器是如果用户没有登录，则跳转到主项目setting中的LOGIN_URL中的值里面去
@login_required #登录权限控制
def home(request):
    #两个参数，第一个是获取的值，第二个是如果获取不到返回的值
    '''username = request.session.get('username','用户未登录')
    print(request.myuser)
    if username =='用户未登录':
        return redirect(reverse('login1'))'''
    #现在不需要session存储用户名，直接使用auth保持登录状态
    #request.user代表用户名
    return render(request,'form_session/home.html',context={
        'username':request.user
    })

class LoginTest(View):
    def get(self,request):
        return render(request,'form_session/login.html')

    def post(self,request):
        username = request.POST.get('usr')
        password = request.POST.get('pwd')
        request.session['username'] = username
        #设置过期时间
        request.session.set_expiry(0) #0表示关闭浏览器后过期
        # return render(request,'form_session/home.html',context={
        #     'username':username
        # })
        return redirect(reverse('home'))

def logout_test(request):
    request.session.flush() #删除当前会话数据并删除会话
    #logout(request) #auth系统退出登录的方法
    return redirect(reverse('home'))


from .forms import RegisterForm
from .models import UserModel
from django.http import HttpResponse
class RegisterTest(View):
    def get(self,request):
        form = RegisterForm()
        return render(request,'form_session/register.html',context={
            'form':form
        })

    def post(self,request):
        #获取表单数据
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            password_confirm = form.cleaned_data.get('password_confirm')
            email = form.cleaned_data.get('email')
            #保存到数据库
            if password == password_confirm:
                #UserModel.objects.create(username=username,password=password,email=email)
                #换成存储User系统中的数据表
                User.objects.create_user(username=username,password=password,email=email)
                return HttpResponse('注册成功，欢迎使用网站')

            else:
                return HttpResponse('注册失败，两次密码不一致')

        else:
            return HttpResponse('注册失败，请输入合法数据')

from .forms import LoginForm
from django.contrib import messages
class Login(View):
    def get(self,request):
        form = LoginForm()
        return render(request,'form_session/login1.html',context={
            'form':form
        })

    def post(self,request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            #查找auth表中的数据
            #user = UserModel.objects.filter(username=username,password=password)
            user = authenticate(username=username,password=password)
            if user:
                #保存登录状态
                #request.session['username'] = username
                #auth方法记住登录状态
                login(request,user)
                # 设置过期时间
                #request.session.set_expiry(0)
                next = request.GET.get('next')  #这里面的next就等于note
                return redirect(reverse('home'))
            else:
                messages.error(request, '登录失败，账户名或者密码不正确')
                return redirect(reverse('login1'))
        else:
            messages.error(request, '请输入正确数据')
            return redirect(reverse('login1'))
