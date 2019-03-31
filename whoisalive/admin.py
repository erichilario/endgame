#admin endgame 1

from django.contrib import admin
from whoisalive.models import Hero, Power

#admin.site.register(Hero)
#admin.site.register(Power)

class PowerInstanceInline(admin.TabularInline):
	model = Power

class HeroAdmin(admin.ModelAdmin):
	inlines = [PowerInstanceInline]
	def hero_power_count(self,obj):
		return obj.power_set.count()
	hero_power_count.short_description = "Power Count"

	list_display = ['hero_name', 'id', 'hero_power_count', 'hero_image', 'hero_description']
	ordering = ('id',)

admin.site.register(Hero, HeroAdmin)

#@admin.register(Power)
#class PowerAdmin(admin.ModelAdmin):
#	list_display = ('power_text', 'hero', 'power_image')
	
	#list_filter = ('hero')