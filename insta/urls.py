from django.urls import path
from . import views
urlpatterns = [
    path('',views.login),
    path('home.html',views.home),
    path('comment.html/',views.save_commentt,name="save_commentt"),
    path('home.html/<str:username>/',views.delete_username,name="delete_user"),
    path('comment.html/<str:comment>/',views.delete_comment,name="delete_comment"),
path('comment.html/',views.comment_view,name="comment"),
    path('payment.html',views.payment,name="payment.html"),
    path('payment_paypal.html',views.payment_paypal),
    path('template.html',views.data_get),
    path('save_username/',views.save_username,name="save_username"),
path('save_time/',views.save_time,name="save_time"),
    path('login_user/',views.login_user,name="login_user"),
    path('logout_user/',views.logout_user,name="logout_user"),
    path('status',views.status_page,name="status"),
path('save_insta',views.save_insta,name="save_insta"),

        
]