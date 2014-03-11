# Create your views here.
from products.forms import ProductForm
from django.http.response import HttpResponseRedirect
from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from .models import products
from django.contrib.auth.decorators import login_required

@login_required(login_url='/log/in/')
def viewCreate(request):
    
    if request.POST: 
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/home/')
    else:
        form = ProductForm()
        
    c = {}
    c.update(csrf(request))
    c['form'] = form
    return render_to_response('createproduct.html', context_instance=RequestContext(request, c))

@login_required(login_url='/log/in/')
def viewUpdate(request, pk):
    id = pk
    if request.POST:
        products.objects.filter(id=id).delete()
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/home/')
    else:
        form = ProductForm()
        
    c = {}
    c.update(csrf(request))
    c['id'] = id
    c['form'] = form
    return render_to_response('update.html', context_instance=RequestContext(request, c))

@login_required(login_url='/log/in/')
def viewDelete(request,pk):
    id = pk
    products.objects.filter(id=id).delete()
    return HttpResponseRedirect('/home/')   
    