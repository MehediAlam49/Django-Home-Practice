from django.contrib import admin
from authApp.models import *
# Register your models here.
class Display_User_List(admin.ModelAdmin):
    list_display=['username','first_name','Education']
    
admin.site.register(custom_student,Display_User_List)