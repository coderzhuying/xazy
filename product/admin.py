from django.contrib import admin
from .models import Housekeeping,Car,People

# Register your models here.

@admin.register(Housekeeping)
class HousekeepingAdmin(admin.ModelAdmin):
    list_display = ['id', 'content','tel']
    list_per_page = 1

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['id', 'content','tel']
    list_per_page = 1


@admin.register(People)
class PeopleAdmin(admin.ModelAdmin):
    list_display = ['id', 'content','tel']
    list_per_page = 1
