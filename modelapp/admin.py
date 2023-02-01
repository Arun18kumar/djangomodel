from django.contrib import admin
from modelapp.models import UserModel

# Register your models here.
@admin.register(UserModel)

class UserAdmin(admin.ModelAdmin):
    list_display = ['name','email']