from django.contrib import admin, messages
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

User = get_user_model()


class UserAdminCustom(UserAdmin):
    model = User
    fieldsets = (
        ('Güvenlik', {
            'fields': ('password', 'verification_token'),
        }),
        ('Tarih', {
            'fields': ('created_at', 'updated_at',),
        }),
        ('İzinler', {'fields': ('groups', 'api_permissions',)}),
        ('Hesap', {
            'fields': ('is_admin', 'is_active',),
        }),
        ('Kişisel', {
            'fields': ('first_name', 'last_name',),
        }),
        ('İletişim', {
            'fields': ('phone', 'email',),
        }),
        ('İletişim İzinleri', {
            'fields': ('email_notification', 'mobile_notification', 'sms_notification',),
        }),

    )
    add_fieldsets = (
        ('Güvenlik', {
            'fields': ('password1', 'password2'),
        }),
        ('Tarih', {
            'fields': ('created_at', 'updated_at',),
        }),
        ('Account Status', {
            'fields': ('is_admin', 'is_active'),
        }),
        ('İzinler', {'fields': ('groups', 'api_permissions')}),

        ('Kişisel', {
            'fields': ('first_name', 'last_name',),
        }),
        ('İletişim', {
            'fields': ('phone', 'email'),
        }),
        ('İletişim İzinleri', {
            'fields': ('email_notification', 'mobile_notification', 'sms_notification',),
        }),

    )
    search_fields = ('is_admin', 'email', 'phone', 'first_name', 'last_name',)
    list_display = ['id', 'first_name', 'last_name', 'email', 'is_active']
    list_display_links = ('id',)
    list_filter = ('is_admin', 'api_permissions', 'created_at', 'is_active',)
    list_editable = ('is_active',)
    readonly_fields = ('created_at', 'updated_at')
    exclude = ('password_reset_token', 'invite_token', 'username',)
    ordering = ('-created_at',)


admin.site.unregister(User)
admin.site.register(User, UserAdminCustom)
