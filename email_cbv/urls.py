from django.conf.urls import patterns, url

from email_cbv import views

urlpatterns = patterns('',
  url(r'^list/$', views.EmailList.as_view(), name='email_list'),
  url(r'^add/$', views.EmailAdd.as_view(), name='email_add'),
)