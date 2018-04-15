# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

SIZE_CHOICES = (
	 ("xl", "XL"),
	 ("l", "L"),
	 ("m", "M"),
	 ("s","S"),
)

STATUS_CHOICES = (
    ('approved', 'Aprobado'),
    ('rejected', 'Rechazado'),
)

class Item(models.Model):
	name = models.CharField(max_length=50)
	size = models.CharField(max_length=50)
	description = models.TextField(max_length=900, null=True, blank=True)
	cost =  models.DecimalField(max_digits=8, decimal_places=2,null=True, blank=True)

	def __unicode__(self):
		return self.name

	def __str__(self):
		return "name:%s, size:%s, cost:%s" %(self.name, self.size, self.cost)

