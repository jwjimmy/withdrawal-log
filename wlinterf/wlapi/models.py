from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Visit(models.Model):
	visited_at = models.DateField()
	reason = models.CharField(max_length=1000)
