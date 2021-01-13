from django.urls import path
from EcomApp import views
from django.contrib.auth import views as v

urlpatterns = [
    path('', views.homeview, name=''),
    path('afterlogin', views.afterloginview, name='afterlogin'),
    path('logout', v.LogoutView.as_view(
        template_name='EcomApp/logout.html'), name='logout'),
    path('adminclick', views.adminclickview),
    path('customer-home', views.customerhomeview, name='customer-home'),
    path('customerlogin', v.LoginView.as_view(
        template_name='EcomApp/clogin.html'), name='customerlogin'),
    path('admin-dashboard', views.admindashboardview, name='admin-dashboard'),
    path('adminlogin', v.LoginView.as_view(
        template_name='EcomApp/alogin.html'), name='adminlogin'),
    path('view-customer', views.viewcustomerview, name='view-customer'),
    path('delete-customer/<int:pk>',
         views.deletecustomerview, name='delete-customer'),
    path('update-customer/<int:pk>',
         views.updatecustomerview, name='update-customer'),
    path('admin-products', views.adminproductsview, name='admin-products'),

    path('admin-add-product', views.adminaddproductview,
         name='admin-add-product'),
    path('delete-product/<int:pk>',
         views.deleteproductview, name='delete-product'),
    path('update-product/<int:pk>',
         views.updateproductview, name='update-product'),
    path('admin-view-booking', views.adminviewbookingview,
         name='admin-view-booking'),
    path('delete-order/<int:pk>', views.deleteorderview, name='delete-order'),

    path('update-order/<int:pk>', views.updateorderview, name='update-order'),
    path('customersignup', views.customersignupview, name='customersignup'),
    path('my-order', views.myorderview, name='my-order'),
    path('my-profile', views.myprofileview, name='my-profile'),
    path('edit-profile', views.editprofileview, name='edit-profile'),
    path('download-invoice/<int:orderID>/<int:productID>',
         views.downloadinvoiceview, name='download-invoice'),
    path('add-to-cart/<int:pk>', views.addtocartview, name='add-to-cart'),
    path('cart', views.cartview, name='cart'),
    path('remove-from-cart/<int:pk>',
         views.removefromcartview, name='remove-from-cart'),
    path('customer-address', views.customeraddressview, name='customer-address'),
    path('payment-success', views.paymentsuccessview, name='payment-success'),
]
