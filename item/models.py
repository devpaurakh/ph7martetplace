from django.contrib.auth.models import User
from django.db import models


class Catagory(models.Model):
    name = models.CharField(max_length=225)
    
    class Meta:
        ordering= ('name',) # to keep the catagories in order
        
        verbose_name_plural = "Catagories"
        
    def  __str__(self):
        return self.name
    

class Item(models.Model):
    catagory = models.ForeignKey(Catagory, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=225)
    description= models.TextField(blank=True,null=True)
    price = models.FloatField()
    image = models.ImageField(upload_to='item_images', blank=True)
    is_sold = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, related_name='item', on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True, null=True)