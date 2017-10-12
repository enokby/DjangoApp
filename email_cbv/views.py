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
