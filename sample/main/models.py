from __future__ import unicode_literals

from django.db import models

# Create your models here.
class SampleData(models.Model):
	name = models.CharField(max_length=30)
	lat = models.DecimalField(decimal_places=6, max_digits=12)
	lon = models.DecimalField(decimal_places=6, max_digits=12)

	def __str__(self):
		return self.name