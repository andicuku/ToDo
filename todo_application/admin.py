from django.contrib import admin

from todo_application.models import ToDo


# Register your models here.

class TodoAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "completed")
    list_filter = ("completed",)


admin.site.register(ToDo, TodoAdmin)
