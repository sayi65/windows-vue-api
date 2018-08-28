from django.contrib import admin
from .models import User, WorkTime
# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass

@admin.register(WorkTime)
class WorkTimeAdmin(admin.ModelAdmin):
    pass