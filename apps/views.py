from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponse
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse_lazy

from email_cbv.models import Email

class EmailList(ListView):
    model = Email

class EmailAdd(CreateView):
    model = Email
    fields = ['name', 'email']
    success_url = reverse_lazy('email_list')

def home(request):
    html = """
    <h1>Django Email App</h1>
    <a href="/list/">List</a><br>
    <a href="/add/add">Add</a><br>      
    """
    return HttpResponse(html)
	
