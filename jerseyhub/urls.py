from django.urls import path
from.import views

urlpatterns=[
    path('about/',views.about,name='about'),
    path('checkout/',views.checkout,name='checkout'),
    path('contact/',views.contact,name='contact'),
    path('index/',views.index,name='index'),
    path('login/',views.user_login,name='login'),
    path('productdetail/',views.productdetail,name='productdetail'),
    path('product/',views.product,name='product'),
    path('shopingcart/',views.shoppingcart,name='shopingcart'),
    path('register/',views.register,name='register')
    


]