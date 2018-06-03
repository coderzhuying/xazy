from django.contrib import admin
from .models import CompanyCulture,CompanyMemorabilia,CompanyProfile,CompanyTeam,CompanyStructure
# Register your models here.

@admin.register(CompanyProfile)
class CompanyProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'content']
    list_per_page = 1

@admin.register(CompanyCulture)
class CompanyCultureAdmin(admin.ModelAdmin):
    list_display = ['id','content']
    list_per_page = 1

@admin.register(CompanyTeam)
class CompanyTeamAdmin(admin.ModelAdmin):
    list_display = ['id','content']
    list_per_page = 1

@admin.register(CompanyMemorabilia)
class CompanyMemorabiliaAdmin(admin.ModelAdmin):
    list_display = ['id','content']
    list_per_page = 1

@admin.register(CompanyStructure)
class CompanyStructureAdmin(admin.ModelAdmin):
    list_display = ['id', 'content']
    list_per_page = 1