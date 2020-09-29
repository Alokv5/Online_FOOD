from django.shortcuts import render,redirect
from foodAdmin.models import AdminLoginModel,StateModel,CusineModel,CityModel
from vendor.models import VendorRegistrationModel
from django.contrib import messages
from foodAdmin.otpsending import sendASMS

def ShowIndex(request):
    return render(request,"foodAdmin/login.html")


def admin_login_check(request):
    if request.method == "POST":
        try:
            admin = AdminLoginModel.objects.get(username=request.POST.get("admin_username"),
                                                password=request.POST.get("admin_password"))
            request.session["admin_status"]= True
            return redirect('welcome')
        except:
            return render(request, "foodAdmin/login.html", {"error": "Invalid User"})
    else:
        request.session["admin_status"] = False
        return render(request, "foodAdmin/login.html", {"error": "Admin Logout "})

def OpenWelcome(request):
    return render(request, "foodAdmin/home.html")

def  Add_state(request):
    return  render(request ,"foodAdmin/state.html",{"stdata":StateModel.objects.all()})

def Add_city(request):
    return render(request, "foodAdmin/city.html",{"ctdata":CityModel.objects.all(),"state":StateModel.objects.only('name')})

def Add_Cuisine(request):
    return render(request, "foodAdmin/cuisine.html",{"cuisine_data":CusineModel.objects.all()})

def Add_Vendor(request):
    return render(request,"foodAdmin/vendor.html",{"Pending":VendorRegistrationModel.objects.filter(status='Pending'),
                                                   "Approved":VendorRegistrationModel.objects.filter(status='Approved'),
                                                   "Cancel":VendorRegistrationModel.objects.filter(status="Cancel")})

def OpenReport(request):
    return render(request,"foodAdmin/report.html")


def save_state(request):
    if request.POST.get('id'):
        sm=StateModel.objects.get(id=request.POST.get('id'))
        sm.name=request.POST.get('state')
        if not request.FILES.get('photo'):
            pass
        else:
            sm.photo = request.FILES.get("photo")
            sm.save()
        return render(request ,'foodAdmin/state.html',{"message":"State Updated","stdata":StateModel.objects.all()})
    else:
        try:
            StateModel.objects.get(name=request.POST.get('state'))
            return render(request,'foodAdmin/state.html',{"error":"State Already Exist","stdata":StateModel.objects.all()})
        except:
            StateModel(name=request.POST.get('state'),photo=request.FILES["photo"]).save()
            messages.success(request,"State Added")
            return redirect('add_state')



def UpdateState(request):
    id=request.GET.get('id')
    sm=StateModel.objects.get(id=id)
    return render(request,'foodAdmin/state.html',
                  {"id":sm.id,"name":sm.name,"photo":sm.photo,"stdata":StateModel.objects.all()})


def Delete_State(request):
        no=request.GET.get("id")
        StateModel.objects.filter(id=no).delete()
        return redirect('add_state')




def save_city(request):
    if request.POST.get('id'):
        cm=CityModel.objects.get(id=request.POST.get('id'))
        cm.name=request.POST.get('city')
        if not request.FILES.get('photo'):
            pass
        else:
            cm.photo = request.FILES.get("photo")
            cm.save()
        return render(request ,'foodAdmin/city.html',{"message":"City Updated",
                                                      "ctdata":CityModel.objects.all(),"state":StateModel.objects.only('name')})
    else:
        try:
            CityModel.objects.get(name=request.POST.get('city'))
            return render(request,'foodAdmin/city.html',{"error":"City Already Exist","ctdata":CityModel.objects.all()})
        except:
            CityModel(name=request.POST.get('city'),photo=request.FILES["photo"],city_state_id=request.POST.get('state')).save()
            messages.success(request,"City Added")
            return redirect('add_city')


def updateCityId(request,id,fkid):
    sm=StateModel.objects.get(id=fkid)
    CityModel.objects.filter(id=id).update(city_state_id=sm.id)


def UpdateCity(request):
    id = request.GET.get("id")
    print(id)
    cm = CityModel.objects.get(id=id)
    return render(request, "foodAdmin/city.html",
                  {"id": cm.id, "city_state":cm.city_state.id, "state_name":cm.city_state.name , "city": cm.name, "photo": cm.photo, "ctdata": CityModel.objects.all(),"state":StateModel.objects.only('name')})


def delete_city(request):
    id=request.GET.get("id")
    CityModel.objects.filter(id=id).delete()
    return redirect('add_city')




def save_cuisine(request):
    if request.POST.get("id"):
        cm=CusineModel.objects.get(id=request.POST.get("id"))
        cm.type=request.POST.get("cuisine")
        if not request.FILES.get("photo"):
            pass
        else:
            cm.photo=request.FILES.get("photo")
        cm.save()
        return render(request,"foodAdmin/cuisine.html",{"success":"Updated Successfully","cuisine_data": CusineModel.objects.all()})
    else:
        try:
            CusineModel.objects.get(type=request.POST.get("cuisine"))
            return render(request, "foodAdmin/cuisine.html",
                          {"error": "Cuisine Already Exist", "cuisine_data": CusineModel.objects.all()})
        except:
            CusineModel(type=request.POST.get("cuisine"), photo=request.FILES.get("photo")).save()
            messages.success(request, "Cuisine Added")
            return redirect('cuisine')


def Update_Cuisine(request):
    id=request.GET.get("id")
    cm=CusineModel.objects.get(id=id)
    return render(request,"foodAdmin/cuisine.html",{"id":cm.id,"cuisine":cm.type,"photo":cm.photo,"cuisine_data":CusineModel.objects.all()})

def delete_cuisine(request):
    id=request.GET.get("id")
    CusineModel.objects.filter(id=id).delete()
    return redirect('cuisine')


def admin_vendor_approve(request):
    res=VendorRegistrationModel.objects.get(id=request.GET.get("id"))
    sname=res.stall_name
    cno=res.contact_1
    res.status='Approved'
    res.save()
    sendASMS(str(cno),"Hello"+sname+"\n Your Registration is Approve Successfully")
    return Add_Vendor(request)


def admin_vender_cancel(request):
    res=VendorRegistrationModel.objects.get(id=request.GET.get("id"))
    res.status="Cancel"
    res.save()
    return Add_Vendor(request)