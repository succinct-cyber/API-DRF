from django.db import models

class Employee(models.Model):
    Emp_id = models.CharField(max_length=20)
    Emp_name = models.CharField(max_length=50)
    Designation = models.CharField(max_length=50)

    def __str__ (self):
        return self.Emp_name
    

# Create your models here.
