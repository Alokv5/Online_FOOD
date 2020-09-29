from django.contrib import admin
from django.urls import path

from customer import views





urlpatterns = [

    path('',views.ShowIndex,name="main"),
    path('customer_register/',views.customer_register,name="customer_register"),
    path('customer_save/',views.customer_save,name="customer_save"),
    path('customer_check_otp/',views.customer_check_otp,name="customer_check_otp"),
    path('customer_login/',views.customer_login,name="customer_login"),
    path('customer_login_check/',views.customer_login_check,name="customer_login_check"),
    path('customer_welcome/<int:pk>', views.customer_welcome, name="customer_welcome"),
    path('customer_logout/',views.customer_login_check,name='customer_logout'),
    path('customer_menu/',views.customer_menu,name="customer_menu"),
    path('add_to_cart/',views.add_to_cart,name="add_to_cart"),
    path('customer_quantity/',views.customer_quantity,name="customer_quantity"),
    path('customer_save_to_cart/',views.customer_save_to_cart,name="customer_save_to_cart"),
    path('customer_cart_items/',views.customer_cart_items,name="customer_cart_items"),
    path('customer_order/',views.customer_order,name="customer_order"),
    path('customer_order_placed/',views.customer_order_placed,name="customer_order_placed"),

]
