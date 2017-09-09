from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm

from .models import User

class UserProfileAdmin(UserAdmin):

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': (
            'first_name',
            'middle_name',
            'last_name',
            'department',
            'course',
            'nick_name',
            'birthdate',
            'mobile_number',
            'age',
            'father_name',
            'mother_maiden_name',
            'address',
            'affiliations',
            'awards',
        )}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    form = UserChangeForm
    list_display = ('email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)
    filter_horizontal = ('groups', 'user_permissions',)
    readonly_fields = ("date_joined",)

admin.site.register(User, UserProfileAdmin)