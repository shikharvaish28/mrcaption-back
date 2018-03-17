from django.shortcuts import render
from django.http import HttpResponse
import requests
# @csrf_exempt
def get_image(request):
    if request.method == 'POST':
        # img = request.POST.get(" image ")
        # return (request)
        # print (request.body)
        img = request.FILES["image"]
        html = "<html><body><h1>hey</h1></body></html>"
        
        return HttpResponse(html)