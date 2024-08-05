from django.shortcuts import render, redirect
from pytube import *

# Create your views here.
from django.shortcuts import render
from pytube import YouTube

def youtube(request):
    if request.method == 'POST':
        # Getting the link from frontend
        link = request.POST['link']
        video = YouTube(link)
        # Setting video resolution
        stream = video.streams.get_highest_resolution()
        # Downloading the video
        stream.download()
        # You might want to handle the case where download fails or provide user feedback
        return render(request, 'youtube.html')
    # Handling GET requests or any other request method
    return render(request, 'youtube.html')
 


