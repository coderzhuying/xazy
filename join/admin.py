from django.contrib import admin
from .models import Recruitment
# Register your models here.

@admin.register(Recruitment)
class RecruitmentAdmin(admin.ModelAdmin):
    list_display = ['id', 'position','requirements','salary','place']
    list_per_page = 1
