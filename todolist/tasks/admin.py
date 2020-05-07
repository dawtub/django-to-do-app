from django.contrib import admin
from .models import Task


class TaskInline(admin.TabularInline):
    model = Task
    extra = 1


class UserAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name']}),
    ]
    inlines = [TaskInline]


class TaskAdmin(admin.ModelAdmin):
    list_display = ('text', 'completed', 'user')
    search_fields = ['user__name']


admin.site.register(Task, TaskAdmin)
