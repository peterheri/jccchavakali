from django.conf.urls import url
from . import views
from django.contrib import admin
from django.contrib.auth import views as auth_views
urlpatterns = [
    url(r'^$', views.home.as_view(), name='home'),
    url(r'^ministries/', views.ministries.as_view(), name='ministries'),
    url(r'^mercy/', views.mercy.as_view(), name='mercy'),
    url(r'^outreach/', views.outreach.as_view(), name='outreach'),
    url(r'^prison/', views.prison.as_view(), name='prison'),
    url(r'^hospital/', views.hospital.as_view(), name='hospital'),
    url(r'^men/', views.men.as_view(), name='men'),
    url(r'^women/', views.women.as_view(), name='women'),
    url(r'^couples/', views.couples.as_view(), name='couples'),
    url(r'^youths/', views.youths.as_view(), name='youths'),
    url(r'^teens/', views.teens.as_view(), name='teens'),
    url(r'^sundayschool/', views.sundayschool.as_view(), name='sundayschool'),
    url(r'^projects/', views.projects.as_view(), name='projects'),
    url(r'^events/', views.events.as_view(), name='events'),
    url(r'^founder/', views.founder.as_view(), name='founder'),
    url(r'^sermons/', views.sermons.as_view(), name='sermons'),
    url(r'^gallery/', views.gallery.as_view(), name='gallery'),
    url(r'^give/', views.give.as_view(), name='give'),
    url(r'^wwn/', views.wwn.as_view(), name='wwn'),
    url(r'^prayer/',views.prayer.as_view(),name='prayer'),
    url(r'^login/$',views.login.as_view(),name='login'),

    ]
