from django.contrib import admin

from .models import UserAccount, UserRelations


@admin.register(UserAccount)
class UserAccountAdmin(admin.ModelAdmin):
    list_display = ["email", "id", "name", "is_active", "is_staff"]


@admin.register(UserRelations)
class UserRelationAdmin(admin.ModelAdmin):
    list_display = ["id", "user"]
