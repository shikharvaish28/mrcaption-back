from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.http import JsonResponse
import requests
# @csrf_exempt
def get_image(request):
    if request.method == 'POST':
        img = request.FILES.get("image")
        path = default_storage.save('mrcaption/image', ContentFile(img.read()))
        print (request.FILES)
        # print (request.body)
        headers  = {'Ocp-Apim-Subscription-Key': '2593b2ee7a9345c7823c2dd3df0f028d',
        "Content-Type": "application/octet-stream" }
        image_data = open(path , "rb").read()
        # params   = {'visualFeatures': 'Categories,Tags'}
        # data     = {'url': "mrcaption/image"}
        vision_url = "https://westcentralus.api.cognitive.microsoft.com/vision/v1.0/analyze?visualFeatures=Categories,Tags&language=en"
        response = requests.post(vision_url, headers=headers, data=image_data)
        data = response.json()
        # print (data)        
        return JsonResponse(data)