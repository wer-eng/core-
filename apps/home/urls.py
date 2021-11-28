# -*- encoding: utf-8 -*-

from django.contrib.auth import views as auth_views
from django.urls import path, re_path
from apps.home import views


urlpatterns = [

    # The home page
    path('', views.index, name='home'),
  
    #users/<int:pk>/
    # Matches any html file
 
    
    path('profil1.html',views.userUpdate, name="profil"),
    path('profil.html/<int:pk>', views.post_update, name='users-edit'),
    path('profilRegister.html',views.userAdd , name="profilEkle"),
    path('usr-ogretmenler.html', views.userShow,name='kullanicilar'),
    path('delete/<int:pk>',views.post_delete, name='delete'),
 
    re_path(r'^.*\.*', views.pages, name='pages'),
]
