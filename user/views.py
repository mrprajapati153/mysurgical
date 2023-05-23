from django.shortcuts import render, HttpResponseRedirect, redirect, HttpResponse
from .forms import Registrationform, addproduct, vender1,query,Shopdetail
from .forms import editprofile
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .models import product
from .models import shop
from django.contrib.auth.models import User
from django.contrib.auth.models import Group, User
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required


# Create your views here.

# index page


def index(request):

    product_item = product.objects.all()

    # serach bar
    item_name = request.GET.get('item_name')
    if item_name != '' and item_name is not None:
        product_item = product_item.filter(product_name__icontains=item_name)

    return render(request, 'user/index.html')

# about page


def about(request):
    return render(request, 'user/about.html')
# contact page


# def contact(request):
#     return render(request, 'user/contact.html')

# products page


def products(request):
    product_item = product.objects.all()

    # serach bar
    item_name = request.GET.get('item_name')
    if item_name != '' and item_name is not None:
        product_item = product_item.filter(product_name__icontains=item_name)
    return render(request, 'user/products.html', {'product_item': product_item})

# product detail view
def product_detail(request, product_id):
    product_item = product.objects.get(product_id=product_id)
    return render(request, 'user/productdetail.html', {'product_item': product_item})


# add product
staff_member_required

def add_product(request):
   
    if request.method == 'POST':
        form = addproduct(request.POST, request.FILES)
    
        if form.is_valid():
            messages.success(request, 'your product has been added')
            form.save()
            return redirect('/shopprofile/')
    else:
        form = addproduct()

    return render(request, 'user/addproduct.html', {'form': form})
# Delete product


@staff_member_required
def delete_product(request, product_id):
  products = product.objects.get(pk=product_id)
  products.delete()
  return redirect('shopprofile')


@staff_member_required
def update_product(request, product_id):
    if request.method == 'POST':
        products = product.objects.get(pk=product_id)
        form = addproduct(request.POST, request.FILES, instance=products)
        if form.is_valid():
           form.save()

    else:
        products = product.objects.get(pk=product_id)
        form = addproduct(instance=products)

    return render(request, 'user/updateproduct.html', {'form': form})


# shop Regisration
def Shop_registraton(request):
    if request.method == "POST":
        form = vender1(request.POST, request.FILES)
        if form.is_valid():
            form.instance.is_staff = True
            form.instance.get_group_permissions()
            user = form.save()
            group = Group.objects.get(name='vender')
            user.groups.add(group)
            return redirect('shopdetail')
    else:
        form = vender1()
    return render(request, 'user/Shopregistraton.html', {'form': form})


#shop detail
def shopdata(request):
   
    if request.method == 'POST':
        form = Shopdetail(request.POST, request.FILES)
    
        if form.is_valid():
            messages.success(request, 'your shop has been added')
            form.save()
            return redirect('/shoplogin/')
    else:
        form = Shopdetail()

    return render(request, 'user/shopdetail.html', {'form': form})



# shop login
def shop_login(request):

    if request.method == "POST":
        fm = AuthenticationForm(request=request, data=request.POST)
        if fm.is_valid():
            uname = fm.cleaned_data['username']
            upass = fm.cleaned_data['password']
            user = authenticate(username=uname, password=upass)
            if user is not None:
                login(request, user)
                messages.success(request, 'Login successfully')
                return HttpResponseRedirect('/shopprofile/')
    else:
        fm = AuthenticationForm()
    return render(request, 'user/shoplogin.html', {'form': fm})

# shop Logout


def shop_logout(request):
    logout(request)
    messages.success(request, 'logout succefully')
    return HttpResponseRedirect('/shoplogin/')

# shop profile


@staff_member_required
def shop_Profile(request):
    products = product.objects.filter(shop_name=request.user)
    return render(request, 'user/shopprofile.html', {'products': products})


# Registration from
def registration(request):
    if request.method == 'POST':
        form = Registrationform(request.POST)
        if form.is_valid():
            messages.success(request, 'your account has been created!!')
            form.save()
    else:
        form = Registrationform()
    return render(request, "user/Registration.html", {'form': form})

# login


def user_login(request):

    if request.method == "POST":
        fm = AuthenticationForm(request=request, data=request.POST)
        if fm.is_valid():
            uname = fm.cleaned_data['username']
            upass = fm.cleaned_data['password']
            user = authenticate(username=uname, password=upass)
            if user is not None:
                login(request, user)
                messages.success(request, 'Login successfully')
                return HttpResponseRedirect('/profile/')
    else:
        fm = AuthenticationForm()
    return render(request, 'user/login.html', {'form': fm})


# logout
@login_required
def user_logout(request):
    logout(request)
    messages.success(request, 'logout successfully')
    return HttpResponseRedirect('/login/')

# profile


@login_required
def profile(request):
    if request.user.is_authenticated:
        if request.method == "POST":

          fm = editprofile(request.POST, instance=request.user)
          if fm.is_valid():
             messages.success(request, 'updated data succedfully')
             fm.save()
        else:
          fm = editprofile(instance=request.user)
        return render(request, 'user/profile.html', {'name': request.user, 'fm': fm})
    else:
        return HttpResponseRedirect('/login/')


# Conatact
def contact1(request):

    if request.method == 'POST':
        form = query(request.POST)

        if form.is_valid():
            messages.success(request, 'your product has been added')
            form.save()
          
    else:
        form = query()

    return render(request, 'user/contact.html', {'form': form})



# #shop login
# def shop_login(request):
#     if request.method == 'POST':
#         email = request.POST['shop_email']
#         password = request.POST['password']
#         user = authenticate(request, shop_email=email, password=password)
#         if user is not None:
#             pass
#             # login(request, user)
#             # return render(request, 'user/shopprofile.html')    
#             # return redirect('shopprofile')
#         else:
#             return render(request, 'user/shopprofile.html', {'error': 'Invalid email or password'})
#     else:
#         return render(request, 'user/shoplogin.html')