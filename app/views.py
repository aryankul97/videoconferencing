from django.shortcuts import render
from django.http import StreamingHttpResponse
from app.camera import VideoCamera, gen

def webcam(request):
	return StreamingHttpResponse(gen(VideoCamera()),content_type='multipart/x-mixed-replace; boundary=frame')

def web(request):
	dic={'data':StreamingHttpResponse(gen(VideoCamera()),content_type='multipart/x-mixed-replace; boundary=frame')}
	return render(request,'web.html',dic)