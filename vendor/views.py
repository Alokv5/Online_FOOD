from django.db.models import QuerySet
from django.shortcuts import render,redirect
from vendor.models import VendorRegistrationModel,FoodtypeModel,FoodItemsModel
from foodAdmin.models import CusineModel,CityModel
from django.contrib import messages
from customer.models import CartItemModel

# Create your views here.
def OpenLogin(request):
    return render(request ,"vendor/login.html")


def vendor_login_check(request):
    if request.method == "POST":
        try:
            vendor_res = VendorRegistrationModel.objects.get(contact_1=request.POST.get("vendor_username"),
                                                          password=request.POST.get("vendor_password"),status='Approved')
            request.session["vendor_status"]= True
            request.session['vendor_id']=vendor_res.id
            return redirect('vendor_welcome',pk=vendor_res.id)
        except Exception as e:
            print(e)
            return render(request, "vendor/login.html", {"error": "Invalid User"})
    else:
        request.session["admin_status"] = False
        return render(request, "vendor/login.html", {"error": "Admin Logout "})


def vendor_register(request):
    return render(request,'vendor/vendor_register.html',{"City":CityModel.objects.all(),"Cuisine":CusineModel.objects.all()})


def save_vendor(request):
    stall=request.POST.get("v1")
    con_1=request.POST.get("v2")
    con_2=request.POST.get("v3")
    ctype=request.POST.get("v4")
    photo=request.FILES.get("v5")
    add=request.POST.get("v6")
    city=request.POST.get("v7")
    pas=request.POST.get("v8")
    OTP=0000
    status='Pending'
    VendorRegistrationModel(stall_name=stall,contact_1=con_1,contact_2=con_2,cuisine_type_id=ctype
                            ,vender_city_id=city,photo=photo,address=add,OTP=OTP,status=status,password=pas).save()
    messages.success(request,"Registration is Completed. Need Aproval by Admin")
    return redirect('vendor_main')


def vendor_welcome(request,pk):
    request.session["vendor_id"] = pk
    vendor_details=VendorRegistrationModel.objects.get(id=pk)
    return render(request,'vendor/home.html',{"vendor_details":vendor_details})



def vendor_food_type(request):
    vendor_details = VendorRegistrationModel.objects.get(id=request.session['vendor_id'])
    return render(request, "vendor/food_type.html",
                  {"vendor_details":vendor_details,'food_type':FoodtypeModel.objects.filter(vender_id_id=request.session['vendor_id'])})


def vendor_logout(request):
    return render(request, "vendor/login.html")


def save_food_type(request):
    FoodtypeModel(name=request.POST.get("f1"),vender_id_id=request.session['vendor_id'],status=request.POST.get('f2')).save()
    return vendor_food_type(request)


def update_food_type(request):
    id=request.GET.get('id')
    print(id)
    fm=FoodtypeModel.objects.get(id=id)
    ftm=FoodtypeModel.objects.all()
    return render(request,'vendor/food_type.html',{"upfoodtype":fm,'data':ftm})

def updatefoodId(request,id,pk):
    FoodtypeModel.objects.get(id=pk)
    FoodtypeModel.objects.filter(id=id).update()

def delete_food_type(request):
    id=request.GET.get('id')
    FoodtypeModel.objects.filter(id=id).delete()
    return redirect('vendor_food_type')


def vendor_food(request):
    vendor_details = VendorRegistrationModel.objects.get(id=request.session['vendor_id'])
    return render(request, "vendor/food.html", {"vendor_details": vendor_details,
                                                     'food_type':FoodtypeModel.objects.filter(vender_id_id=request.session['vendor_id']),
                                                'food':FoodItemsModel.objects.filter(food_type__vender_id=request.session["vendor_id"])})


def vendor_save_food(request):
    FoodItemsModel(name=request.POST.get("f1"),food_type_id=request.POST.get("f2"),price=request.POST.get('f3'),photo=request.FILES['f4']).save()
    return vendor_food(request)


def vendor_customer_order(request):
    vender_id_id = request.session['vendor_id']
    v_id = request.session['vendor_id']
    res=CartItemModel.objects.filter(status='Order',food__food_type__vender_id=v_id)
    q=CartItemModel.objects.filter(status='Order',food__food_type__vender_id=v_id).query
    q.group_by=['customer_id']
    res=QuerySet(query=q,model=CartItemModel)
    print(res)
    return render(request ,'vendor/customer_order.html',{"data":res})
