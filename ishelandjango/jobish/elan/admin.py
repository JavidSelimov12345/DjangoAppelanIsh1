from django.contrib import admin
from .models import Elan,Categories







# Register your models here.

class ElanInline(admin.TabularInline):
    model = Elan

class ElanAdmin(admin.ModelAdmin):
    list_display = ('title','image_field')
    search_fields = ['title',]
    list_filter = ('title',)
   

class CotegoryAdmin(admin.ModelAdmin):
    list_display = ('Categori_name',)
    list_filter = ('Categori_name',)
    search_fields = ['Categori_name',]
    # inlines = [ElanInline,]
admin.site.register(Elan, ElanAdmin)
admin.site.register(Categories,CotegoryAdmin)



