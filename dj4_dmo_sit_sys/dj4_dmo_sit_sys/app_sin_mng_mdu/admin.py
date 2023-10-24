from django.contrib import admin
from .models import SigninLog


# Register your models here.
@admin.register(SigninLog)
class SigninLogAdmin(admin.ModelAdmin):
    list_display = ("id", "user_id", "username", "first_name", "last_name", "signin_datetime", )

