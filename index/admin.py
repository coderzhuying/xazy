from django.contrib import admin
from .models import Notice,BigImage,SamllImage
# Register your models here.

@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):
    list_display = ['id','title', 'content','pub_date']
    list_per_page = 1

@admin.register(BigImage)
class BigImageAdmin(admin.ModelAdmin):
    list_per_page = 1

@admin.register(SamllImage)
class SamllImageAdmin(admin.ModelAdmin):
    list_per_page = 1


