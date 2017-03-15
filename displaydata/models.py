from django.db import models

# Create your models here.
class DisplayData(models.Model):
	url = models.CharField(max_length=220, )
	shortcode = models.CharField(max_length=15, default='cfdefaultvalue', unique=True)

	def __str__(self):
		return str(self.url)

	def __unicode__(self):
		return str(self.url)