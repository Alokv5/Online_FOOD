from django.contrib import admin
from django.urls import path

from vendor import views

urlpatterns = [
    path('',views.OpenLogin,name="vendor_main"),
    path('vendor_login_check/',views.vendor_login_check,name='vendor_login_check'),
    path('vendor_register/',views.vendor_register,name='vendor_register'),
    path('save_vendor/',views.save_vendor,name="save_vendor"),
    path('vendor_welcome/<int:pk>',views.vendor_welcome,name="vendor_welcome"),
    path('vendor_logout/',views.vendor_logout,name="vendor_logout"),
    path('vendor_food_type/',views.vendor_food_type,name="vendor_food_type"),
    path('save_food_type/',views.save_food_type,name="save_food_type"),
    path('update_food_type/',views.update_food_type,name="update_food_type"),
    path('updatefoodId/',views.updatefoodId,name="updatefoodId"),
    path('delete_food_type/',views.delete_food_type,name="delete_food_type"),
    path('vendor_food/',views.vendor_food,name="vendor_food"),
    path('vendor_save_food/',views.vendor_save_food,name="vendor_save_food"),
    path('vendor_customer_order/',views.vendor_customer_order,name="vendor_customer_order")


]
