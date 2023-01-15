import sys
import os
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'instagram.settings')
django.setup()
from insta.models import *
from django.contrib.auth.models import User
from bot.InstagramBot import *

def main2():
    obj=User.objects.all().values()
    for i in list(obj):
        print(i['username'])
    obj2=Details.objects.all().values()
    for j in list(obj2):
        print(j)
    obj = Setting.objects.filter(username="admin").values()[0]
    print(obj)
if __name__ == "__main__":
    main2()

