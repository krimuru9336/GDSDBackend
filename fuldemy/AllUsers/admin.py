from django.contrib import admin

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import FuldemyUser
#, user_type


class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password', 'first_name', 'last_name', 'registration_date','is_teacher','is_student','profile_pic')}),
        ('Permissions', {'fields': (
            'is_staff',
            'is_superuser',
            'groups',
            'user_permissions',
        )}),
    )


    list_display = ('email', 'password', 'first_name', 'last_name', 'is_staff', 'registration_date','is_teacher','is_student','profile_pic')
    list_filter = ('is_staff', 'is_superuser', 'groups')
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ('groups', 'user_permissions',)


admin.site.register(FuldemyUser, UserAdmin)
#admin.site.register(user_type)

