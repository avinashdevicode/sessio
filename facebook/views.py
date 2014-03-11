'''
Created on Mar 10, 2014

@author: avinash
'''

from django.http.response import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.contrib.auth.views import logout, login
from django.contrib.auth import authenticate
from django.core.context_processors import csrf
from products.models import products
from django.contrib.auth.decorators import login_required


def viewLogin(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username= username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/home/')
    elif request.user.is_authenticated():
        return HttpResponseRedirect('/home/')
    else:
        return render_to_response('login.html', context_instance= RequestContext(request))

@login_required(login_url='/log/in/')
def viewHome(request):
    all_products = products.objects.all()
    c = {}
    c['products']= all_products
    return render_to_response('home.html', context_instance= RequestContext(request, c))

@login_required(login_url='/log/in/')
def viewLogout(request):
    logout(request)
    return HttpResponseRedirect('/log/in/')