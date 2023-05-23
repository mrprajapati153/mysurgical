from user.models import product,Contact,shop
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm




# Registration form
class Registrationform(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email',]
        labels = {'email': 'Email'}

class addproduct(forms.ModelForm):
    class Meta:
        model=product
        fields = ['shop_name', 'product_name','product_image1','product_image2','product_manufeacture','product_modelno','prodect_detail','product_type','product_price','contact']
        # fields = '__all__'
        
class Shopdetail(forms.ModelForm):
    class Meta:
        model=shop
        fields = ['shop_name','shop_address','shop_city','shop_state','shop_country','shop_pincode','shop_mobile','shop_Background_photo','shop_otherphoto','shop_pancardno','shop_GST']
class vender1(UserCreationForm):
      
    class Meta:
        model = User
        fields = ['username','email','password1', 'password2']
        labels = {'email': 'Email'}
        
class editprofile(UserChangeForm):
    password=None
    class Meta:
        
        model=User
        fields=['username','first_name','last_name','email',]
        labels={'email':'Email'}
        
        
class query(forms.ModelForm):
    class Meta:
        model=Contact
        fields='__all__'