
from django.db import models

class Campaign(models.Model):

	name = models.CharField(max_length=140)
	subheading = models.CharField(max_length=140)
	desc = models.TextField()
	handle = models.CharField(max_length=40)