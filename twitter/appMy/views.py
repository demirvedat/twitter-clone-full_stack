from django.shortcuts import render,redirect
from .models import *
# Create your views here.
def index(request):
    tweets=Tweet.objects.all()
    if request.method == 'POST':
        if request.FILES:
            text=request.POST['text']
            image=request.FILES['image']
        
            tweet=Tweet(user=request.user,text=text,image=image)
            tweet.save()
            return redirect('index')
        else:
            text=request.POST['text']
        
            tweet=Tweet(user=request.user,text=text)
            tweet.save()
            return redirect('index')
        
         
       
    context={
            'tweets':tweets,
        }
    return render(request,'index.html',context)
    
    
    


def Explore(request):
    
    return render(request,'explore.html')


def Profile(request):
    
    return render(request,'profile.html')

def Userprofile(request):
    
    return render(request,'userprofile.html')

def Twitter(request):
    
    return render(request,'twitter.html')