from django.contrib import admin
from .models import CompanyNews,LocalNews,MediaNews
# Register your models here.

@admin.register(CompanyNews)
class CompanyNewsAdmin(admin.ModelAdmin):
    list_display = ['id','title','author','content','pub_date','img']
    list_filter = ['title']
    list_per_page = 1

@admin.register(LocalNews)
class LocalNewsAdmin(admin.ModelAdmin):
    list_display = ['id','title','author','content','pub_date','img']
    list_filter = ['title']
    list_per_page = 1

@admin.register(MediaNews)
class MediaNewsAdmin(admin.ModelAdmin):
    list_display = ['id','title','author','content','pub_date','img']
    list_filter = ['title']
    list_per_page = 1

admin.site.site_header = "西安庄勇物业有限公司"
admin.site.site_title = "后台管理"

