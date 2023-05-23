from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator
from django.core.files import File

# Create your models here.

class shop(models.Model):
 
    shop_name = models.OneToOneField(User, on_delete=models.CASCADE)
    # shop_name=models.CharField(max_length=50)
    shop_address=models.CharField(max_length=100)
    shop_city=models.CharField(max_length=50)
    shop_state=models.CharField(max_length=50)
    shop_country=models.CharField(max_length=50)
    shop_pincode=models.PositiveIntegerField(validators=[MaxValueValidator(999999)])
    shop_mobile=models.PositiveIntegerField(validators=[MaxValueValidator(9999999999)])
    shop_Background_photo=models.ImageField(upload_to='shop_picture/')
    shop_otherphoto=models.ImageField(upload_to='shop_picture/')
    shop_pancardno=models.CharField(max_length=10)
    shop_GST=models.CharField(max_length=50)
   
    
     
    def __str__(self):
        return str(self.shop_name)
 
    
class product(models.Model):
    product_id=models.IntegerField(primary_key=True)
    # shop_id=models.ForeignKey(shop, on_delete=models.CASCADE)
    shop_name = models.ForeignKey(User,on_delete=models.CASCADE)
    product_name=models.CharField(max_length=100)
    product_image1=models.ImageField(upload_to='product_picture/')
    product_image2=models.ImageField(upload_to='product_picture/')
    product_manufeacture=models.CharField(max_length=100)
    product_modelno=models.PositiveBigIntegerField(validators=[MaxValueValidator(111111111111)])
    prodect_detail=models.CharField(max_length=100)
    product_type=models.CharField(max_length=50)
    product_price=models.FloatField(max_length=10)
    contact=models.IntegerField()
    def __str__(self):
        return str(self.shop_name)
    
class Contact(models.Model):
    name=models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
