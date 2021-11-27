from django.contrib import admin
from .models import  Profile


class AdminProfile(admin.ModelAdmin):
    list_display=('image_tag','name' , 'title', 'description' , 'price','Product_id' )
    
admin.site.register(Profile,AdminProfile)




