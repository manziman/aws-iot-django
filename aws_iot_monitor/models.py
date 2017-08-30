# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Device(models.Model):
	# Attirbutes
	devid = models.CharField(max_length=10)

	# Methods
	def __str__(self):
		return self.devid