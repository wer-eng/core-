# -*- encoding: utf-8 -*-
"""
Copyright (c) 2021 - present RoboBusters
"""
from django.db.models import manager
from django.http.response import Http404
from django.urls.base import reverse_lazy
from django.views.generic import  UpdateView
from django.forms.forms import Form
from django.shortcuts import get_object_or_404, render,redirect
from django.contrib import messages
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.conf import settings
from django.views.generic.edit import DeleteView
from apps.authentication.forms import LoginForm
from apps.home.form import ProfilDetayForm
from apps.home.models  import ProfilDetay,JobsTable
from django.contrib.auth.models import User
from django.views.generic.detail import DetailView
@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:
        pass
        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))

def userShow(request):
    users = ProfilDetay.objects.all()
    context = {
        'Kullanicilar' : users,
        'media_url':settings.MEDIA_URL
    }
    
    return render(request,'home/usr-ogretmenler.html',context)
def userAdd(request):
    user=request.user
    if request.method == "POST":
        newUser = ProfilDetayForm(request.POST)
        if newUser.is_valid():
            newUser.save()
            return HttpResponseRedirect('/')
    else:
        newUser = ProfilDetayForm()
    context={
        'user':user,
        'newUser' :newUser,
        'media_url':settings.MEDIA_URL}
    return render(request,'home/profilRegister.html',context)



def post_update(request,pk):
    
    
    

    post = get_object_or_404(ProfilDetay, id=pk)
    
    form = ProfilDetayForm(request.POST or None, request.FILES or None, instance=post)
    if form.is_valid():
        form.save()
        
        return HttpResponseRedirect('/')
    
    user = User.objects.get(id=pk)
    detail = ProfilDetay.objects.get(user=user)
    jobs =  JobsTable.objects.all()
    form = ProfilDetayForm(instance=post)
  
    context={
        'user':user,
        'detail':detail,
        'jobs':jobs,
        'form':form,
        'media_url':settings.MEDIA_URL
        }
    

    return render(request, "home/profil.html", context)


   

def userUpdate(request):
    id= request.user.id
    user = User.objects.get(id=id)
    detail = ProfilDetay.objects.get(user=user)
    jobs =  JobsTable.objects.all()
    form = ProfilDetayForm()
    context={
        'user':user,
        'detail':detail,
        'jobs':jobs,
        'form':form,
        'media_url':settings.MEDIA_URL
    }
    return render(request,'home/profil1.html',context)

def post_delete(request, pk):
    user = User.objects.get(id=pk)
    if not request.user.is_authenticated:
        # Eğer kullanıcı giriş yapmamış ise hata sayfası gönder
        return Http404()

    post = get_object_or_404(ProfilDetay, id=pk)
    post.delete()
    user.delete()
    return HttpResponseRedirect("/")

