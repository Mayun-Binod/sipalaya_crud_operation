from django.contrib import admin
from crud_app.models import Student_Detail
# Register your models here.
@admin.register(Student_Detail)
class StudentAdmin(admin.ModelAdmin):
    list_display=['full_name','age','email','message']


