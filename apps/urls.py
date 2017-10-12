from django.conf.urls import include, url
from django.contrib import admin

from email_cbv import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'apps.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^list/$', views.EmailList.as_view(), name='email_list'),
	url(r'^add/$', views.EmailAdd.as_view(), name='email_add'),
    url(r'^$', 'apps.views.home'),
]
