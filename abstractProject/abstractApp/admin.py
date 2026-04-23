from django.contrib import admin
from abstractApp.models import *
# Register your models here.
class Display_user_list(admin.ModelAdmin):
    list_display=['username','userType','DisplayName']
    
admin.site.register(custom_user,Display_user_list)