from django.contrib import admin
from .models import *

# Register your models here.
class RegionAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug':('name',)} # slug field를 name field 값에 따라 자동으로 설정.

class PlaceAdmin(admin.ModelAdmin):
    list_display = ['region', 'name', 'image', 'slug']
    prepopulated_fields = {'slug': ('name',)} # slug field를 name field 값에 따라 자동으로 설정.

admin.site.register(Region, RegionAdmin)
admin.site.register(Place, PlaceAdmin)