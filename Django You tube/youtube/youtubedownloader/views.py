from django.shortcuts import render
from django.contrib import messages
from pytube import *

# Create your views here.
def index(request):
    if request.method=="POST":
        url=request.POST['url']
        video=YouTube(url)
        stream=video.streams.get_highest_resolution()
        stream.download()
        messages.info(request,'video downloaded')
        return render(request,'index.html')
    return render(request,'index.html')    