from django.urls import path
from . import views
urlpatterns = [
    path('',views.login),
    path('home.html',views.home),
    path('comment.html/',views.save_commentt,name="save_commentt"),
path('comment.html/',views.comment,name="comment"),
    path('payment.html',views.payment,name="payment.html"),
    path('payment_paypal.html',views.payment_paypal),
    path('template.html',views.data_get),
    path('save_username/',views.save_username,name="save_username"),
    path('login_user/',views.login_user,name="login_user"),

        
]