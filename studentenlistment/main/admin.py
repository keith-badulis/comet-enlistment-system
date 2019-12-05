from django.contrib import admin
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin

from .models import *


class ProfileInLine(admin.StackedInline):
    model = Profile
    verbose_name_plural = 'Profiles'


class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
    )

    list_display = ('username', 'first_name', 'last_name', 'id_number', 'type', 'college')
    inlines = [ProfileInLine]

    def id_number(self, obj):
        return obj.profile.id_number

    def type(self, obj):
        return obj.profile.type

    def college(self, obj):
        return obj.profile.college


class ClassAdmin(admin.ModelAdmin):
    list_display = ('course', 'section_code', 'start_time', 'end_time', 'day', 'student_count', 'max_cap')

    @staticmethod
    def student_count(obj):
        return obj.students.count()


class ProgramInLine(admin.StackedInline):
    model = Program
    verbose_name_plural = 'Programs'


class CollegeAdmin(admin.ModelAdmin):
    list_display = ('name', 'short')
    inlines = [ProgramInLine]


class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_name', 'subject_area', 'catalog_num', 'units')


admin.site.site_header = 'Amino Acids Administration'
admin.site.site_title = 'Amino Acids'
admin.site.index_title = 'Administrator'

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

admin.site.register(College, CollegeAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Class, ClassAdmin)

admin.site.unregister(Group)

# Register your models here.
