from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin

class MyException(MiddlewareMixin):
    def process_request(self,request):
        #print('中间件process_request被调佣')
        request.name = 'bojun'
        #下面的HttpResponse会拦截请求到达视图层
        #return HttpResponse(111)
        #如果想要照常到达视图层，换成None值
        return None

class UserMiddleware(MiddlewareMixin):
    def __init__(self,get_response):
        self.get_response = get_response

    def __call__(self,request):
        #请求到达视图之前
        username = request.session.get('username','用户未登录')
        if username == '用户未登录':
            setattr(request,'myuser',username)
        else:
            setattr(request, 'myuser', '用户未登录')
        #print('===========request===========')

        #相应返回给用户之前
        reponse = self.get_response(request)
        #print('============reponse============')
        #把正常相应返回给用户
        return reponse