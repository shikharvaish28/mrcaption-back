from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
import requests
# @csrf_exempt
def get_image(request):
    if request.method == 'POST':
        img = request.FILES["image"]
        path = default_storage.save('mrcaption/image', ContentFile(img.read()))
        # print (type(img))
        headers  = {'Ocp-Apim-Subscription-Key': '2593b2ee7a9345c7823c2dd3df0f028d',
        "Content-Type": "application/json" }
        image_data = open('mrcaption/image', "rb").read()
        # params   = {'visualFeatures': 'Categories,Tags'}
        # data     = {'url': "mrcaption/image"}
        vision_url = "https://westcentralus.api.cognitive.microsoft.com/vision/v1.0/analyze?visualFeatures=Categories,Tags&language=en"
        response = requests.post(vision_url, headers=headers, data=image_data)
        print (response.json())
        html = "<html><body><h1>hey</h1></body></html>"
        
        return HttpResponse(html)