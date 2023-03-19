from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from appMy.models import *
from appUser.models import *

# Create your views here.
def likes(request):
    tweetid = request.POST['tweetid']
    tweet = Tweet.objects.get(id = tweetid)
    
    if 'like' in request.POST:
        if Tweet.objects.filter(like__in = [request.user], id = tweetid).exists():
            tweet.like.remove(request.user)
            tweet.save()
        else:
            tweet.like.add(request.user)
            tweet.save()
        
def loginUser(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            message='Kullanıcı adı veya Şifre hatalı'
            return render(request,'user/login.html',{'message':message})
    return render(request,'user/login.html')


def registerUser(request):
    
     if request.method == "POST":
        name=request.POST["name"]
        surname=request.POST["surname"]
        email=request.POST["email"]
        username=request.POST["username"]
        password1=request.POST["password1"]
        password2=request.POST["password2"]
        
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                message = 'Bu kullanıcı adı zaten alınmış'
                return render(request,'user/register.html',{'message':message})
            elif User.objects.filter(email=email).exists():
                message='Bu email başkası tarafından kullanılıyor'
                return render(request,'user/register.html',{'message':message})
            else:
                user=User.objects.create_user(first_name=name,last_name=surname,email=email,username=username,password=password1)
                user.save()
                return redirect('loginUser')
        else:
            message='Şifreler eşleşmiyor'
            return render(request,'user/register.html',{'message':message})
     return render(request,'user/register.html')
 
 
def logoutUser(request):
    logout(request)
    return redirect('Twitter')

def Profile(request):
    user = request.user
    shared = Tweet.objects.filter(owner = request.user)
    liked = Tweet.objects.filter(like__in = [request.user])
    r_user=User.objects.all().order_by('?')[:5]
    if request.method == 'POST':
        if 'rfollow' in request.POST:
            userid=request.POST['userid']
            ruser=User.objects.get(id=userid)
            if request.user.is_authenticated:
                account=Userinfo.objects.get(user=request.user)
                if Userinfo.objects.filter(user = request.user, follow__in = [ruser]).exists():
                    account.follow.remove(ruser)
                    ruser.userinfo.follower.remove(request.user)
                    account.save()
                else:
                        account.follow.add(ruser)
                        ruser.userinfo.follower.add(request.user)
                        account.save()
                        
        elif request.method == 'POST':
            likes(request)
    
    context={
        'user':user,
        'shared':shared,
        'liked':liked,
        'r_user':r_user,
    }
    
    
    return render(request,'profile.html',context)



def Userprofile(request,pk):
    user = User.objects.get(id = pk)
    shared = Tweet.objects.filter(owner = user)
    liked = Tweet.objects.filter(like__in = [user])
    r_user=User.objects.all().order_by('?')[:5]
    
  
    if request.method == 'POST':
        
        if 'follow' in request.POST:
            if request.user.is_authenticated:
                myaccount = Userinfo.objects.get(user = request.user)
                
                if Userinfo.objects.filter(user = request.user, follow__in = [user]).exists():
                    myaccount.follow.remove(user)
                    user.userinfo.follower.remove(request.user)
                    myaccount.save()
                else:
                    myaccount.follow.add(user)
                    user.userinfo.follower.add(request.user)
                    
                    myaccount.save()
                    
        elif request.method == 'POST':
            likes(request)
        return redirect('Userprofile',pk = user.id)
    
    
    context={
        'user':user,
        'shared':shared,
        'liked':liked,
        'r_user':r_user,
    }
    
    return render(request,'userprofile.html',context)