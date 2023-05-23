from .import views
from django.urls import path

urlpatterns = [
    path('',views.index,name='index'),
    path('registration/',views.registration,name='registration'),
    path('login/',views.user_login,name='login'),
    path('logout/',views.user_logout,name='logout'),
    path('profile/',views.profile,name='profile'), 
      
#     path('products/',views.products,name='products'),
#     path('addproduct/',views.add_product,name='addproduct'),
#     path('products/<int:id>/',views.product_detail,name='product_detail'),
# 
]

