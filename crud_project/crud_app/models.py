from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
import uuid
# Create your models here.
class Student_Detail(models.Model):
    pk_id=models.UUIDField(primary_key=True,default=uuid.uuid4)
    full_name=models.CharField(max_length=200)
    age=models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    email=models.EmailField(max_length=200,unique=True,null=True)
    message=models.CharField(max_length=255)
    isdelete=models.BooleanField(default=False)
