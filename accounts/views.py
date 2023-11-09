from django.shortcuts import render,redirect # error (import redirect)
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect,HttpResponse
from .models import Profile
from products.models import *
from accounts.models import Cart , CartItems
from django.http import HttpResponseRedirect


# Create your views here.


def login_page(request):

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_obj = User.objects.filter(username = email)

        if not user_obj.exists():
            messages.warning(request, "Account not found.")
            return HttpResponseRedirect(request.path_info)

        if not user_obj[0].Profile.is_email_verified:  # error (profile == Profile)
            messages.warning(request, "Your account is not verified.")
            return HttpResponseRedirect(request.path_info)

        user_obj = authenticate(username = email , password = password)
        if user_obj:
            login(request , user_obj)
            return redirect('/') # error (uper import nhi kiya == redirect ko)

        messages.warning(request, "InValid credentails.")
        return HttpResponseRedirect(request.path_info)
    return render(request ,'accounts/login.html')

def register_page(request):

    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user_obj = User.objects.filter(username = email)

        if user_obj.exists():
            messages.warning(request, "Email is already taken.")
            return HttpResponseRedirect(request.path_info)
        
        print(email)

        user_obj = User.objects.create(first_name = first_name , last_name = last_name , email = email , username = email)
        user_obj.set_password(password)
        user_obj.save()

        messages.success(request, "An email has been sent on your mail.")
        return HttpResponseRedirect(request.path_info)

        # send_mail(
        # 'Subject here',
        # 'Here is the message.',
        # 'saadsheikh131959@gmail.com',
        # ['abdbasitali313595@gmail.com'],
        # fail_silently=False,
        # )
    return render(request ,'accounts/register.html')



def activate_email(request , email_token):
    try:
        user = Profile.object.get(email_token= email_token)
        user.is_email_verified = True
        user.save()
        return redirect('/')
    
    except Exception as e:
        return HttpResponse('Invalid Email Token')
    


def add_to_cart(request , uid):
    variant = request.GET.get('variant')
    product = Product.objects.get(uid=uid)
    user = request.user
    cart , _ =Cart.objects.get_or_create(user = user , is_paid = False)

    cart_item = CartItems.objects.create(cart = cart , product = product , )

    if variant:
        variant = request.GET.get('variant')
        size_variant = SizeVariant.objects.get(size_name = variant)
        cart_item.size_variant = size_variant
        cart_item.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    #return render(request,'cart.html')




def remove_cart(request , cart_item_uid):
    try:
        cart_item = CartItems.objects.get(uid = cart_item_uid)
        cart_item.delete()
    except Exception as e:
        print(e)
    
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))




def cart(request):
    context = {'.cart': Cart.objects.filter(is_paid = False , user = request.user)}
    return render(request , 'accounts/cart.html',context)
