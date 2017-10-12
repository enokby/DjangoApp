from django.db import models
from django.core.urlresolvers import reverse


class Email(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=255)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('email_cbv:add', kwargs={'pk': self.pk})