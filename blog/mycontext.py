def my_user(request):
    user = request.session.get('username','用户未登录')
    if user != '用户未登录':
        return {'myuser':user}
    else:
        return {'myuser':'用户未登录，请先登录'}
