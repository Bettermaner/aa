from django.shortcuts import render
from redis.client import StrictRedis
from django.http import HttpResponse


# Create your views here.
def set_session(request):
    rs = StrictRedis(host='localhost', port=6379, db=0)
    request.session['username'] = 'admin'
    request.session['password'] = '123'

    return HttpResponse('设置成功')


def get_session(request):
    name = request.session.get('username')
    password = request.session.get('password')

    return HttpResponse('%s %s' % (name, password))
