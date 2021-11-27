from django.db import models
from django.utils.html import format_html

# Create your models here.
class Profile(models.Model):
    Product_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=90)
    title=models.CharField(max_length=90)
    description=models.TextField()
    price=models.FloatField(max_length=9)
    image=models.ImageField(upload_to='images')

    def __str__(self):
     return self.name
    

    def image_tag(self):
        return format_html('<img src="/media/{}" style="width:40px;height:40px;border-radius:50%" />'.format(self.image))

