from django.contrib import admin
from . models import Gallery

class GalleryAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'day_publish')


admin.site.register(Gallery, GalleryAdmin)