from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreatoinForm, CustomUserChangeFrom
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreatoinForm
    form = CustomUserChangeFrom
    list_display = ['username', 'email', 'post', 'is_staff', 'age']
    model = CustomUser


admin.site.register(CustomUser, CustomUserAdmin)