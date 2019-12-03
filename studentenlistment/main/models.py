from django.db import models
from django.contrib.auth.models import User


class College(models.Model):
    name = models.CharField(max_length=50)
    short = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Program(models.Model):
    name = models.CharField(max_length=50)
    short = models.CharField(max_length=10)
    college = models.OneToOneField(College, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


class Course(models.Model):
    course_name = models.CharField(max_length=50)
    subject_area = models.CharField(max_length=2)
    catalog_num = models.CharField(max_length=5)
    units = models.FloatField()

    def __str__(self):
        return self.course_name


class Class(models.Model):
    M = 1
    T = 2
    W = 3
    H = 4
    F = 5
    MW = 6
    TH = 7
    DAY_CHOICES = (
        (M, 'Monday'),
        (T, 'Tuesday'),
        (W, 'Wednesday'),
        (H, 'Thursday'),
        (F, 'Friday'),
        (MW, 'Monday and Wednesday'),
        (TH, 'Tuesday and Thursday'),
    )
    students = models.ManyToManyField(User, blank=True)
    course = models.OneToOneField(Course, null=True, on_delete=models.SET_NULL)
    section_code = models.CharField(max_length=5)
    max_cap = models.IntegerField(default=0)
    start_time = models.TimeField()
    end_time = models.TimeField()
    day = models.IntegerField(choices=DAY_CHOICES)

    def __str__(self):
        return '%s (%s)' % (self.course, self.section_code)


class Profile(models.Model):
    UNACTIVATED = 0
    ADMIN = 1
    STUDENT = 2
    USER_TYPE_CHOICES = (
        (UNACTIVATED, 'unactivated'),
        (ADMIN, 'admin'),
        (STUDENT, 'student'),
    )

    user = models.OneToOneField(User, unique=True, null=False, db_index=True, on_delete=models.CASCADE)
    type = models.IntegerField(default=0, choices=USER_TYPE_CHOICES)
    slug = models.SlugField(default='hello-world')

    id_number = models.IntegerField(default=0, unique=True)
    college = models.OneToOneField(College, on_delete=models.CASCADE, blank=True, null=True)
