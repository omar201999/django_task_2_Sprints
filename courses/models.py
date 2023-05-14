from django.db import models

# Create your models here.


class Courses(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(default="anyThing", null=True, blank=True)
    instructor_name = models.CharField(max_length=255)
    numbers_of_students = models.IntegerField(max_length=1000)
