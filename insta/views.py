from django.shortcuts import render,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import views as auth_views
from .models import *
from django.contrib import messages,auth
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


# Create your views here.
def logout_view(request):
   
   return render(request,'index.html')

def login(request):
   # return render(request, "index.html")
   return render(request, "index.html")   

def home(request):
   return render(request,'home.html')
@login_required(login_url='/login')
def comment(request):
   return render(request,'comment.html')
@login_required(login_url='/login')
def payment_paypal(request):
   return render(request,'payment_paypal.html')
@login_required(login_url='/login')
def payment(request):
   return render(request,'payment.html')
@login_required(login_url='/login')
@csrf_exempt
def login_user(request):
   print("run")
   if request.method == 'POST':
      username = request.POST['email']
      password = request.POST['password']
      user = auth.authenticate(username=username, password=password)
      if user is not None:
         if user.is_active:
            auth.login(request, user)
         
         return render(request,'home.html')
      else:
         # messages.error(request,'Invalid')
         return render(request,'login')
   else:
      return render(request, 'account/index.html')

def save_commentt(request):
   print("Saving comment")
   if request.method=="POST":
      name=request.POST.get('comment')
      current_user = request.user
      print(current_user.id)
      print(name)
      ab=Comments(comment=name,user_email=current_user)
      print(ab)
      ab.save()
   return render(request, "comment.html")

def save_username(request):
   if request.method=="POST":
      current_user = request.user
      print(current_user.id)
      name=request.POST.get('username')
      from_time=request.POST.get('from')
      to_time=request.POST.get('to')
      # account=request.POST.get('')
      print(name)
      en=Details(user_email=name,from_time=from_time,to_time=to_time,account=current_user)
      print(en)
      en.save()
   return render(request, "home.html")

def data_get(request):
   data=Details.objects.all().values()
   print(data)
   template=loader.get_template('template.html')
   context={'mymembers':data}
   return HttpResponse(template.render(context,request))