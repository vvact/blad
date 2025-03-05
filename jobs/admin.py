from django.contrib import admin
from .models import Job,Category

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'location', 'deadline', 'is_featured', 'created_at')
    list_filter = ('is_featured', 'deadline')
    search_fields = ('title', 'company', 'location')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']