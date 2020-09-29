from django.contrib import admin
from django.urls import path
from foodAdmin import views

urlpatterns = [
    path('',views.ShowIndex,name="main"),
    path('admin_login_check/',views.admin_login_check,name="admin_login_check"),
    path('welcome/',views.OpenWelcome,name="welcome"),

    path('add_state/', views.Add_state, name="add_state"),
    path('add_city/', views.Add_city, name="add_city"),
    path('add_cuisine/', views.Add_Cuisine, name="add_cuisine"),
    path('add_vendor/', views.Add_Vendor, name="add_vendor"),
    path('add_report/', views.OpenReport, name="add_report"),
    path('logout/', views.admin_login_check,name="logout"),


     path('save_state/', views.save_state, name="save_state"),
    path('state_update/', views.UpdateState, name="state_update"),

     path('delete_state/', views.Delete_State, name="delete_state"),
     path('save_city/', views.save_city, name="save_city"),
     path('update_city/', views.UpdateCity, name="update_city"),
     path('delete_city/', views.delete_city, name="delete_city"),
     path('save_cuisine/', views.save_cuisine, name="save_cuisine"),
     path('update_cuisine/', views.Update_Cuisine, name="update_cuisine"),
     path('delete_cuisine/', views.delete_cuisine, name="delete_cuisine"),


    path('admin_vendor_approve/',views.admin_vendor_approve,name="admin_vendor_approve"),
    path('admin_vender_cancel/',views.admin_vender_cancel,name="admin_vender_cancel")


]