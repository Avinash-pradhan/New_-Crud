from django.db import models

# Create your models here.

class Student(models.Model):
    student  = models.CharField(max_length=100)
    number = models.IntegerField()
    email = models.EmailField()
    degree = models.CharField(max_length=100)
    yop = models.IntegerField()

    def __str__(self):
        return self.student