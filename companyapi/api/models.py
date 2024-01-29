from django.db import models


# Create your models here.


# Create your company models here.
class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=224)
    location = models.CharField(max_length=224)
    about = models.TextField()
    type = models.CharField(max_length=224, choices=(('IT', 'IT'),
                                                     ('NON IT', 'NON IT'),
                                                     ("MOBILES PHONES", 'MOBILE PHONES')
                                                     ))
    added_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name + self.location


# employee models
class Employee(models.Model):
    name = models.CharField(max_length=224)
    email = models.EmailField(max_length=224)
    address = models.CharField(max_length=224)
    phone = models.CharField(max_length=224)
    about = models.TextField()
    position = models.CharField(max_length=224, choices=(
        ('Manager', 'manager'),
        ('Software Developer', 'sd'),
        ('Project Leader', 'pl')
    ))
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
