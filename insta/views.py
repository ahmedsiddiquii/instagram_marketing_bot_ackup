from django.shortcuts import render,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import views as auth_views
from .models import *
from django.contrib import messages,auth
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect



# Create your views here.

def login(request):
   # return render(request, "index.html")
   return render(request, "index.html")   

@login_required(login_url='/')
def home(request):
   obj=Details.objects.filter(user_email=request.user).values_list("account")
   obj=list(obj)
   for i in range(len(obj)):
      obj[i]=obj[i][0]

   time_obj=Time.objects.filter(user_email=request.user).values()
   if len(list(time_obj))>=1:
      time_obj=list(time_obj)[0]
      from_time=time_obj['from_time']
      to_time=time_obj['to_time']
      context={"emails":list(obj),"from_time":from_time,"to_time":to_time,"user":str(request.user).capitalize()}
   else:
      context = {"emails": list(obj),'user':str(request.user).capitalize()}
   print("home")
   return render(request,'home.html',context)

@login_required(login_url='/')
def status_page(request):
   try:
      obj = Setting.objects.filter(username=request.user).values()[0]
      status= obj['status']
      insta_user=obj['insta_id']
      insta_password=obj["insta_pass"]
      context={"status":status,"insta_id":insta_user,"insta_pass":insta_password}
   except:
      context={"status":"Off","insta_id":"","insta_pass":""}

   return render(request,'status.html',context)

@login_required(login_url='/')
def save_insta(request):
   if request.method=="POST":
      insta_username=request.POST['insta_id']
      insta_password=request.POST['insta_pass']
      obj=Setting.objects.get(username=request.user)
      obj.insta_id=insta_username
      obj.insta_pass=insta_password
      obj.save()
   return redirect(status_page)

@login_required(login_url='/')
def comment_view(request):
   obj=Comments.objects.filter(user_email=request.user).all().values()

   return render(request,'comment.html',{'comments':list(obj)})

def payment_paypal(request):
   return render(request,'payment_paypal.html')

def payment(request):
   return render(request,'payment.html')


def logout_user(request):
   print("logout")
   if request.method == 'POST':
      auth.logout(request)
   return redirect(login)

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
         
         return redirect(home)
      else:
         # messages.error(request,'Invalid')
         return redirect(login)
   else:
      return redirect(home)

def save_commentt(request):

   if request.method=="POST":
      print("Saving comment")
      name=request.POST.get('comment')
      current_user = request.user
      print(current_user.id)
      print(name)
      ab=Comments(comment=name,user_email=current_user)
      print(ab)
      ab.save()
   return comment_view(request)


def save_time(request):
   if request.method=="POST":
      Time.objects.filter(user_email=request.user).delete()
      current_user = request.user
      print(current_user.id)
      from_time=request.POST.get('from')
      to_time=request.POST.get('to')
      # account=request.POST.get('')

      en=Time(user_email=current_user,from_time=from_time,to_time=to_time)
      en.save()
      return redirect(home)
def save_username(request):
   if request.method=="POST":
      current_user = request.user
      print(current_user.id)
      name=request.POST.get('username')

      # account=request.POST.get('')
      print(name)
      en=Details(user_email=current_user,account=name)
      print(en)
      en.save()
   return redirect(home)

def data_get(request):
   data=Details.objects.all().values()
   print(data)
   template=loader.get_template('template.html')
   context={'mymembers':data}
   return HttpResponse(template.render(context,request))

def delete_username(request,username=None):
   print(request.method)
   print(username)
   Details.objects.filter(account=username,user_email=request.user).delete()
   return redirect(home)

def delete_comment(request,comment=None):
   print(request.method)
   print(comment)
   Comments.objects.filter(user_email=request.user,comment=comment).delete()
   return redirect(comment_view)