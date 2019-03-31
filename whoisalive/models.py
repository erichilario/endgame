from django.db import models
from django.urls import reverse
from django.conf.urls.static import static

class Hero(models.Model):
	hero_name = models.CharField(max_length=50, default='The Hero\'s Name')
	hero_image = models.ImageField(upload_to='static/whoisalive/images', default='static/whoisalive/images/default.png')
	hero_description = models.TextField(max_length=500, default='Description')
	
	def __str__(self):
		return self.hero_name

	def get_absolute_url(self):
		return reverse('hero-detail', args=[str(self.id)])

	class Meta:
		verbose_name = 'Hero'
		verbose_name_plural = 'Heroes'

class Power(models.Model):
	power_text = models.TextField(max_length=200)
	hero = models.ForeignKey(
		Hero,
		on_delete=models.CASCADE,
		verbose_name="hero power"
	)
	power_image = models.ImageField(upload_to='static/whoisalive/pics', default='static/whoisalive/pics/default.png')

	def __str__(self):
		return self.power_text
	
	class Meta:
		ordering = ('power_text',)