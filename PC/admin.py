from django.contrib import admin
from django.contrib.auth import admin as admin_auth_django
from PC.forms import UserChangeForm, UserCreationForm
from PC.models import *

@admin.register(Usuario)
class UsersAdmin(admin_auth_django.UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    model = Usuario
    fieldsets = admin_auth_django.UserAdmin.fieldsets + (
        ('cidade', {'fields': ('cidade',)}),
        ('tipo', {'fields': ('tipo',)}),
    )

admin.site.register(Patrimonio)
admin.site.register(Comentario)