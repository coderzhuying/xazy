from django.contrib import admin
from .models import Information
# Register your models here.

@admin.register(Information)
class InfomationAdmin(admin.ModelAdmin):
    list_display = ['id', 'telephone','address','person']
    list_per_page = 1

