from django.contrib import admin
from .models import House
# Register your models here.

@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    list_display = ['id','title','content','pub_date','author','img']
    list_per_page = 1
