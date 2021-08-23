from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Item(models.Model):
    user_name=models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    Item_name=models.CharField(max_length=200)
    Item_desc=models.CharField(max_length=200)
    Item_price=models.IntegerField()
    Item_image=models.CharField(max_length=500,default="https://www.food4fuel.com/wp-content/uploads/woocommerce-placeholder-600x600.png")

    
    def get_absolute_url(self):
        return reverse("details", kwargs={"pk": self.pk})
    


   





# def __str__(self):
#     return self.Item_nameder_food_item_2.png