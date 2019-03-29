#admin endgame 1

from django.contrib import admin
from whoisalive.models import Hero, Trivia

#admin.site.register(Hero)
#admin.site.register(Trivia)

class TriviaInstanceInline(admin.TabularInline):
	model = Trivia

class HeroAdmin(admin.ModelAdmin):
	inlines = [TriviaInstanceInline]
	def hero_trivia_count(self,obj):
		return obj.trivia_set.count()
	hero_trivia_count.short_description = "Trivia Count"
	list_display = ['hero_name', 'id', 'hero_trivia_count', 'hero_image']
	ordering = ('id',)

admin.site.register(Hero, HeroAdmin)

#@admin.register(Trivia)
#class TriviaAdmin(admin.ModelAdmin):
#	list_display = ('trivia_text', 'hero', 'trivia_image')
	
	#list_filter = ('hero')