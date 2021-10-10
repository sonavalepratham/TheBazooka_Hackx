from django.shortcuts import render, HttpResponseRedirect,reverse,HttpResponse
from django.db import connection
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from .models import extenduser, SymptomsInfo
import csv
from django.conf import settings
from django.core.mail import send_mail
# Create your views here.

def index(request):
    if request.user.is_authenticated:
        return render(request,'chatbot.html')
    return HttpResponseRedirect(reverse('login'))

def team(request):
    return render(request,'index.html')

def Register(request):
    if request.method=="POST":
        usrnm=request.POST['email']
        passwrd1= request.POST['pass1']
        passwrd2 = request.POST['pass2']
        usrnm = request.POST['email']
        f_nm = request.POST['f_nm']
        email = request.POST['email']
        l_nm = request.POST['l_nm']
        age = request.POST['age']
        sex = request.POST['sex']
        if passwrd1==passwrd2:
            user = User.objects.create_user(username=usrnm, password=passwrd1, email=email, last_name=l_nm, first_name=f_nm)
            user.save()
            if user is not None:
                prev=extenduser(Sex=sex, Age=age, user_id=user.id)
                prev.save()
                return HttpResponse('Account Created SuccessFully, Now You Can Login')
            else:
                return HttpResponse('Error') 
        else:
            return HttpResponse('Password not match')
    return render(request,'registration.html')

def HandleLogin(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('index'))

    if request.method=="POST":
        usrnm=request.POST['usrnm']
        passwrd= request.POST['pass']
        user= authenticate(username=usrnm,password=passwrd)
        if user is not None:  
            login(request,user)
            return HttpResponseRedirect(reverse('index'))
        else:
            return HttpResponseRedirect(reverse('index'))
    else:
        return render(request,'login.html')

def HandleLogout(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))

def storesymptoms(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            sym_str=request.POST['ipstr']
            ipstr=request.POST['ipstr']
            ipstr=ipstr.split()
            val=0
            arr={}
            with open('hash.csv', 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    try:
                        if row[0].strip() is not None:
                            arr[row[0]]=row[1]
                    except:
                        pass
            for tmpstr in ipstr:
                if tmpstr.strip() in arr:
                    val+=int(arr[tmpstr.strip()])

            dis_lst=[]
            with open('processed_disease.csv', 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    try:
                        if int(row[0])==val:
                            dis_lst.append(row[1])
                    except:
                        pass
            sym=SymptomsInfo(user_id=request.user.id, symptoms=sym_str)
            try:
                print(set(dis_lst))
                sym.pos_dis=dis_lst[0]
                danger_dis=['Pneumonia', 'Heart attack']
                dis_lst[0]='Pneumonia'
                if dis_lst[0] in danger_dis:
                    msg=request.user.get_full_name()+" is suffering from "+dis_lst[0]
                    send_mail('Danger Disease', msg, 'bazookahackx@gmail.com', ['sonavaleps@gmail.com'], fail_silently=False,)

            except:
                sym.pos_dis="Not able to detect"
            sym.save()
        return HttpResponseRedirect(reverse('table'))
    return HttpResponseRedirect(reverse('login'))

def Table(request):
    if request.user.is_authenticated:
        sym_obj=SymptomsInfo.objects.filter(user_id=request.user.id)
        lr=[]
        cnt=0
        for i in sym_obj:
            if cnt%2==0:
                lr.append("left")
            else:
                lr.append("right")
            cnt+=1
        return render(request,'table.html', {'syo':zip(sym_obj, lr)})
    return HttpResponseRedirect(reverse('login'))

def pharmacy(request):
    return render(request,'carousel.html')