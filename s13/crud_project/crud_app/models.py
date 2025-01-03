from django.db import models
from django.core.validators import MinLengthValidator
# Create your models here.

class Student(models.Model):
    name=models.CharField(max_length=200,validators=[MinLengthValidator(5)])
    age=models.IntegerField()
    email=models.EmailField(unique=True)
    message=models.TextField()
    isdelete=models.BooleanField(default=False)