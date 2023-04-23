from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser
from django.utils.html import format_html

# @admin.display(description='Username')
# def upperUsername(obj):
#     return f"{obj.username}".capitalize()


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        "email",
        'upperUsername',
        "age",
        "is_staff",
    ]
    fieldsets = UserAdmin.fieldsets + (
        (None, {
            "fields": (
                "age",
            ),
        }),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {
            "fields": (
                "age",
            ),
        }),
    )

    @admin.display(description='Username')
    def upperUsername(self, obj):
        return f"{obj.username}".capitalize()


admin.site.register(CustomUser, CustomUserAdmin)
