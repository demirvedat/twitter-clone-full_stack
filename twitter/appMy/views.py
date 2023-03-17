from django.shortcuts import render,redirect
from .models import *
from appUser.models import *
from django.contrib.auth import authenticate
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
            
            
def index(request):
    tweets=Tweet.objects.all().order_by('-id')
    if 'share' in request.POST:
        
        if request.method == 'POST':
            if request.FILES:
                text=request.POST['text']
                image=request.FILES['image']
                
                tweet=Tweet(owner=request.user,text=text,image=image)
                tweet.save()
                return redirect('index')
            else:
                text=request.POST['text']

                
                tweet=Tweet(owner=request.user,text=text)
                tweet.save()
                return redirect('index')
            
    if request.method == 'POST':
        likes(request)
       
    context={
            'tweets':tweets,
            
        }
    return render(request,'index.html',context)
    
    
    


def Explore(request):
    tweets=Tweet.objects.all().order_by('-id')
    r_user=User.objects.all().order_by('?')[:5]
    if request.method == 'POST':
        userid=request.POST['userid']
        ruser=User.objects.get(id=userid)
        if 'rfollow' in request.POST:
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
    
    
    context ={
        'r_user':r_user,
        'tweets':tweets,
    }
    
    return render(request,'explore.html',context)






def Twitter(request):
    
    return render(request,'twitter.html')