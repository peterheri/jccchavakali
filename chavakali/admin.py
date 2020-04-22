from django.contrib import admin
from .models import *
from django.contrib.admin import ModelAdmin
from django.contrib import admin


class SlideshowsAdmin(ModelAdmin):
	"""docstring for SlideshowsAdmin"""
	list_display = ("name","image")
admin.site.register(Slideshows,SlideshowsAdmin)

class MercyimageoneAdmin(ModelAdmin):
	"""docstring for MercyimageoneAdmin"""
	list_display = ("name", "image")
admin.site.register(Mercyimageones, MercyimageoneAdmin)

class HomemissionAdmin(ModelAdmin):
	"""docstring for HomemissionAdmin"""
	list_display = ("name", "image")
admin.site.register(Homemission, HomemissionAdmin)

class MercycoverAdmin(ModelAdmin):
	""""docstring for MercycoverAdmin"""
	list_display = ("name", "image")
admin.site.register(Mercycover, MercycoverAdmin)

class MercyfooterAdmin(ModelAdmin):
	""""docstring for MercyfooterAdmin"""
admin.site.register(Mercyfooter,MercyfooterAdmin)

class MencoverAdmin(ModelAdmin):
	""""docstring for MencoverAdmin"""
admin.site.register(Mencover, MencoverAdmin)

class MenfooterAdmin(ModelAdmin):
	""""docstring for Menfooter"""
admin.site.register(Menfooter,MenfooterAdmin)

class WomencoverAdmin(ModelAdmin):
	""""docstring for Womencover"""
admin.site.register(Womencover,WomencoverAdmin)

class WomenfooterAdmin(ModelAdmin):
	""""docstring for Womencover"""
admin.site.register(Womenfooter, WomenfooterAdmin)

class CouplescoverAdmin(ModelAdmin):
	""""docstring for Couplescover"""
admin.site.register(Couplescover, CouplescoverAdmin)

class CouplesfooterAdmin(ModelAdmin):
	""""docstring for Couplesfooter"""
admin.site.register(Couplesfooter, CouplesfooterAdmin)

class YouthcoverAdmin(ModelAdmin):
	""""docstring for Youthcover"""
admin.site.register(Youthcover, YouthcoverAdmin)

class YouthfooterAdmin(ModelAdmin):
	""""docstring for Youthfooter"""
admin.site.register(Youthfooter, YouthfooterAdmin)

class TeenscoverAdmin(ModelAdmin):
	""""docstring for Teenscover"""
admin.site.register(Teenscover, TeenscoverAdmin)

class TeensfooterAdmin(ModelAdmin):
	""""docstring for Teensfooter"""
admin.site.register(Teensfooter, TeensfooterAdmin)

class SundayschoolcoverAdmin(ModelAdmin):
	""""docstring for sundayschoolcover"""
admin.site.register(Sundayschoolcover, SundayschoolcoverAdmin)

class SundayschoolfooterAdmin(ModelAdmin):
	""""docstring for sundayschoolfooter"""
admin.site.register(Sundayschoolfooter, SundayschoolfooterAdmin)

class WwncoverAdmin(ModelAdmin):
	""""docstring for Wwwcover"""
admin.site.register(Wwncover, WwncoverAdmin)

class WwnfooterAdmin(ModelAdmin):
	""""docstring for Wwwfooter"""
admin.site.register(Wwnfooter, WwnfooterAdmin)

class BishopAdmin(ModelAdmin):
	""""docstring for Bishop"""
admin.site.register(Bishop, BishopAdmin)

class ReverendAdmin(ModelAdmin):
	""""docstring for Reverend"""
admin.site.register(Reverend, ReverendAdmin)

class EventoneAdmin(ModelAdmin):
	""""docstring for Eventone"""
admin.site.register(Eventone, EventoneAdmin)

class EventtwoAdmin(ModelAdmin):
	""""docstring for Eventwo"""
admin.site.register(Eventtwo, EventtwoAdmin)

class EventthreeAdmin(ModelAdmin):
	""""docstring for Eventone"""
admin.site.register(Eventthree, EventthreeAdmin)

class ProjectoneAdmin(ModelAdmin):
	""""docstring for Projectone"""
admin.site.register(Projectone, ProjectoneAdmin)

class ProjecttwoAdmin(ModelAdmin):
	""""docstrong for Projecttwo"""
admin.site.register(Projecttwo, ProjecttwoAdmin)

class ProjectthreeAdmin(ModelAdmin):
	""""docstring for Projectthree"""
admin.site.register(Projectthree, ProjectthreeAdmin)

class DroneAdmin(ModelAdmin):
	""""docstring for Drone"""
admin.site.register(Drone, DroneAdmin)

class logoAdmin(ModelAdmin):
	""""docstring for logo"""
admin.site.register(logo, logoAdmin)
