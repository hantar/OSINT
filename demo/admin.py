from django.contrib import admin
from .models import Datacrawl
from .models import Category
# Register your models here.
class DatacrawlAdmin(admin.ModelAdmin):
    list_display = ('type', 'text', 'username', 'url', 'created', 'added')

class CategoryAdmin(admin.ModelAdmin):
    pass
admin.site.register(Category, CategoryAdmin)
admin.site.register(Datacrawl, DatacrawlAdmin)