from django.db import models
from .utils import code_generator, create_shortcode

# Create your models here.
# from displaydata.models import DisplayData; DisplayData.objects.refresh_shortcodes()
class DisplayDataManager(models.Manager):
	def all(self, *args, **kwargs):
		return super(DisplayDataManager, self).all(*args,**kwargs).filter(active=True)

	def refresh_shortcodes(self):
		qs = DisplayData.objects.filter(id__gte=1)
		new_codes = 0
		for q in qs:
			q.shortcode = create_shortcode(q)
			print(q.shortcode)
			q.save()
			new_codes += 1
		return "New codes made: {i}".format(i=new_codes)

class DisplayData(models.Model):
	url       = models.CharField(max_length=220, )
	shortcode = models.CharField(max_length=15, unique=True, blank=True)
	updated   = models.DateTimeField(auto_now_add=True) # Everytime the model is saved
	timestamp = models.DateTimeField(auto_now_add=True) # When model was created
	active    = models.BooleanField(default=True) # Is active

	objects = DisplayDataManager()

	def save(self, *args, **kwargs):
		if self.shortcode is None or self.shortcode == "":
			self.shortcode = create_shortcode(self)
		super(DisplayData, self).save(*args, **kwargs)

	def __str__(self):
		return str(self.url)

	def __unicode__(self):
		return str(self.url)