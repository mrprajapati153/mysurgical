from django.contrib import admin
from user.models import shop,product,Contact
# Register your models here.

class shopAdmin(admin.ModelAdmin):
    list_display=['shop_name','shop_address','shop_city','shop_state','shop_country','shop_pincode','shop_mobile','shop_Background_photo','shop_pancardno','shop_GST']
admin.site.register(shop,shopAdmin)
 
class productAdmin(admin.ModelAdmin):
    list_display=['shop_name','product_name','product_image1','product_manufeacture','product_modelno','prodect_detail','product_type','product_price']
admin.site.register(product,productAdmin)

class ContactAdmin(admin.ModelAdmin):
    list_display=['name','email','subject','message']
admin.site.register(Contact,ContactAdmin)

