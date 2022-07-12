from django.contrib import admin
from .models import Page
@admin.register(Page)
class PgaeAdmin(admin.ModelAdmin):
    list_display = ['page_name','page_cat','page_publish_date','user']