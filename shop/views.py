from django.shortcuts import render
from .models import Profile
from .forms import ImageProfile

def Profiles(request):
    if request.method=="POST":
        fm=ImageProfile(request.POST ,request.FILES)
        if fm.is_valid():
            fm.save()
    fm=ImageProfile()
    img=Profile.objects.all()        
    return render(request , 'index.html' , {'img':img})            


       

