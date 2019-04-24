from django.contrib import admin
from .models import WebLinks
# Register your models here.
class WebLinksAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'created', 'updated')
admin.site.register(WebLinks, WebLinksAdmin)
