from django.contrib import admin

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.apps import apps
from .models import MessageModel
from django.contrib.admin import ModelAdmin, site
from .models import MessageModel

from .models import FuldemyUser,Skills
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


#admin.site.register(FuldemyUser, UserAdmin)
#admin.site.register(user_type)


class MessageModelAdmin(ModelAdmin):
    readonly_fields = ('timestamp',)
    search_fields = ('id', 'body', 'user__username', 'recipient__username')
    list_display = ('id', 'user', 'recipient', 'timestamp', 'characters')
    list_display_links = ('id',)
    list_filter = ('user', 'recipient')
    date_hierarchy = 'timestamp'


#site.register(MessageModel, MessageModelAdmin)


admin.site.register(apps.all_models['AllUsers'].values())

