from django.contrib import admin
from foodapp.models import Item

# Register your models here.
class display(admin.ModelAdmin):
    list_display=['Item_name']


admin.site.register(Item,display)