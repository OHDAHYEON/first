from django.contrib import admin
from market.models import *

# Register your models here.
@admin.register(Cate)
class CateAdmin(admin.ModelAdmin):
    list_display = ('cate_name',)

@admin.register(Market)
class MarketAdmin(admin.ModelAdmin):
    list_display = ('cate', 'image', 'item_name', 'price')

