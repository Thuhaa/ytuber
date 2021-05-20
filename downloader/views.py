from django.shortcuts import render
from django.http import HttpResponse
from pytube import YouTube

def homepage_view(request):
	return render(request, 'downloader/homepage.html')

def get_video_view(request):
	url = request.GET.get('url')
	yt = YouTube(str(url))
	title = yt.title
	thumbnail = yt.thumbnail_ur
	context = {'title':title, 'thumbnail':thumbnail}
	return render(request, 'downloader/preview.html', context)