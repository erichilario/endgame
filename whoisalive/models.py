from django.db import models
from django.urls import reverse

class Hero(models.Model):
	hero_name = models.CharField(max_length=50)
	hero_image = models.ImageField(upload_to='pics', default='static/whoisalive/images/background2.jpg')
	
	def __str__(self):
		return self.hero_name

	def get_absolute_url(self):
		return reverse('hero-detail', args=[str(self.id)])

	class Meta:
		verbose_name = 'Hero'
		verbose_name_plural = 'Heroes'

class Trivia(models.Model):
	trivia_text = models.TextField(max_length=200)
	hero = models.ForeignKey(
		Hero,
		on_delete=models.CASCADE,
		verbose_name="hero trivia"
	)
	trivia_image = models.ImageField(upload_to='pics', default='pics/default.png')

	def __str__(self):
		return self.trivia_text
	
	class Meta:
		ordering = ('trivia_text',)