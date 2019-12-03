from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

from .models import *


class ProfileInLine(admin.StackedInline):
    model = Profile
    verbose_name_plural = 'Profiles'


class CustomUserAdmin(UserAdmin):
    list_display =('username', 'first_name', 'last_name', 'id_number', 'type', 'college')
    inlines =[ProfileInLine]

    def id_number(self, instance):
        return instance.profile.id_number

    def type(self, instance):
        return instance.profile.type

    def college(self, instance):
        return instance.profile.college


class ClassAdmin(admin.ModelAdmin):
    verbose_name_plural = 'Classes'


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

admin.site.register(College)
admin.site.register(Program)
admin.site.register(Course)
admin.site.register(Profile)
admin.site.register(Class, ClassAdmin)


# Register your models here.
