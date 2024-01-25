from django.db import models


# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100,null='True',verbose_name="student name")
    email = models.EmailField(max_length=227,null='True',verbose_name="student email")


    def __str__(self):
        return str(self.id)