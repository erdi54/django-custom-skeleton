from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

User = get_user_model()


@admin.register(User)
class AccountsAdmin(UserAdmin):
    fieldsets = (
        ('Güvenlik', {
            'fields': ('password',),
        }),
        ('Tarih', {
            'fields': ('created_at', 'updated_at', 'last_login'),
        }),
        ('İzinler', {'fields': ('groups', 'user_permissions',)}),
        ('Hesap', {
            'fields': ('is_admin', 'is_staff', 'is_active', 'api_permissions'),
        }),
        ('Kişisel', {
            'fields': ('first_name', 'last_name'),
        }),
        ('İletişim', {
            'fields': ('email',),
        }),

    )
    add_fieldsets = (
        ('Güvenlik', {
            'fields': ('password1', 'password2'),
        }),
        ('Tarih', {
            'fields': ('created_at', 'updated_at', 'last_login',),
        }),
        ('Account Status', {
            'fields': ('is_admin', 'is_staff', 'is_active', 'api_permissions'),
        }),
        ('İzinler', {'fields': ('groups', 'user_permissions',)}),
        ('Kişisel', {
            'fields': ('first_name', 'last_name'),
        }),
        ('İletişim', {
            'fields': ('email',),
        }),

    )
    search_fields = ('is_admin', 'email', 'first_name', 'last_name')
    list_display = ['first_name', 'last_name', 'email', 'last_login', 'is_active']
    list_display_links = ('first_name', 'last_name', 'email',)
    list_filter = ('is_admin',)
    list_editable = ('is_active',)
    exclude = ('password_reset_token', 'invite_token')
    readonly_fields = ('last_login', 'created_at', 'updated_at')
