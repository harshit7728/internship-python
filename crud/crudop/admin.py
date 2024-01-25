from django.contrib import admin

from crudop.models import Student


# Register your models here.
@admin.register(Student)
class studentAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "email"]
