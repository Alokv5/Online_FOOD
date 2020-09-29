from django.shortcuts import render,redirect
from customer.middleware import returnAddress
from vendor.models import FoodItemsModel
from django.core.paginator import Paginator
from customer.models import CityModel,CustomerRegistrationModel,CartItemModel,OrderModel
import random
from  foodAdmin.otpsending import sendASMS

def ShowIndex(request):

       data=FoodItemsModel.objects.all()
       res=returnAddress()
       page_no=request.GET.get("pageno",1)
       p=Paginator(data,3)
       if page_no:
           page=p.page(page_no)
       else:
           page=p.page(1)
       return render(request, "customer/main.html", {"address":res[0], "city":res[1], "food":page})


def customer_register(request):
     return render(request,'customer/register.html',{"city":CityModel.objects.all()})


def customer_save(request):
    name=request.POST.get("c1")
    contact=request.POST.get("c2")
    ad=request.POST.get("c3")
    ct=request.POST.get("c4")
    pas=request.POST.get("c5")
    otp=random.randint(100000,999999)
    print(otp)
    message="Hello"+name+",Welcome to online Food Services \n To complete Registration to use this OTP"+str(otp)
    sendASMS(contact,message)
    CustomerRegistrationModel(name=name,contact=contact,address=ad,city_id=ct,password=pas,otp=otp).save()
    return render(request,"customer/otp.html",{"contactno":contact})


def customer_check_otp(request):
    try:
        CustomerRegistrationModel.objects.get(contact=request.POST.get('cno'),otp=request.POST.get('otp'))
        return render(request, 'customer/welcome.html')

    except CustomerRegistrationModel.DoesNotExist:
        return render(request, 'customer/otp.html',{"contactno":request.POST.get('cno'),"message":"Invalid OTP"})


def customer_login(request):
    return render(request ,'customer/login.html')


def customer_login_check(request):
    if request.method == "POST":
        try:
            res = CustomerRegistrationModel.objects.get(contact=request.POST.get("c1"),password=request.POST.get("c2"))

            request.session["customer_status"] = True
            request.session["customer_id"] = res.id
            return redirect('customer_welcome', pk=res.id)
        except CustomerRegistrationModel.DoesNotExist:

            return render(request, "customer/login.html", {"error": "Invalid User Or Password"})
    else:
        request.session["customer_status"]=False
        return render(request, "customer/login.html", {"error": "Customer  Logout Success "})


def customer_welcome(request,pk):
    request.session["customer_id"] = pk
    customer_details = CustomerRegistrationModel.objects.get(id=pk)
    return render(request, 'customer/home.html', {"customer_details": customer_details})


def customer_menu(request):
    customer_details = CustomerRegistrationModel.objects.get(id=request.session["customer_id"])
    data = FoodItemsModel.objects.all()
    res = returnAddress()
    page_no = request.GET.get("pageno", 1)
    p = Paginator(data, 3)
    if page_no:
        page = p.page(page_no)
    else:
        page = p.page(1)

    return render(request , 'customer/menu.html',{"customer_details": customer_details,"address": res[0], "city": res[1], "food": page})

def add_to_cart(request):
     if request.session['customer_status']:
          item_id=request.POST.get('item')
          food= FoodItemsModel.objects.get(id=item_id)
          total=food.price
          return render(request ,'customer/addcart.html',{"food":food,"count":1,"total":total})

     else:
          return redirect('customer_login')

count=0
total=0
def customer_quantity(request):
    b=request.POST.get('b1')
    price=float(request.POST.get('price'))
    global count,total

    if b == '+':
        count+=1
        total= price*count
    else:
        if count >0:
            count-=1
            total = price * count

    item_id = request.POST.get('item')
    food = FoodItemsModel.objects.get(id=item_id)
    return render(request, 'customer/addcart.html', {"food": food,"count":count,"total":total})


def customer_save_to_cart(request):
    item_id=request.POST.get('item_id')
    count=request.POST.get('count')
    c_id=request.session['customer_id']
    CartItemModel(customer_id=c_id,food_id=item_id,quantity=count,status='Active').save()
    return redirect('customer_menu')


def customer_cart_items(request):
    customer_details = CustomerRegistrationModel.objects.get(id=request.session["customer_id"])
    c_id = request.session['customer_id']
    cart_items=CartItemModel.objects.filter(customer_id=c_id,status='Active')
    return render(request, 'customer/cart_items.html',{"cart_items":cart_items,"customer_details": customer_details})


def customer_order(request):
    address=request.POST.get("address")
    total=request.POST.get("total")
    c_id = request.session['customer_id']
    OrderModel(address=address,total=total,c_id_id=c_id).save()

    data=CartItemModel.objects.filter(customer_id=c_id).update(status="Order")

    return redirect('customer_order_placed')


def customer_order_placed(request):
    c_id = request.session['customer_id']
    cart_items= CartItemModel.objects.filter(customer_id=c_id,status="Order")
    return render(request,'customer/order.html',{"cart_items":cart_items})