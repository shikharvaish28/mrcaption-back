from django.shortcuts import render
import requests
import wikiquotes
from watson_developer_cloud import ToneAnalyzerV3
import json
from aylienapiclient import textapi
from django.http import HttpResponse
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.http import JsonResponse
import requests
# @csrf_exempt
def get_image(request): 
    if request.method == 'POST': #check if the method of call is post
        img = request.FILES.get("image") #store the image in a variable by calling the 'POST' request
        path = default_storage.save('mrcaption/image', ContentFile(img.read())) #save the image in the storage 
        # print (request.FILES)  #this prints the image name and all the details that come along 
        headers  = {'Ocp-Apim-Subscription-Key': '2593b2ee7a9345c7823c2dd3df0f028d',
        "Content-Type": "application/octet-stream" }
        image_data = open(path , "rb").read() #locate the path and open the file
        vision_url = "https://westcentralus.api.cognitive.microsoft.com/vision/v1.0/analyze?visualFeatures=Categories,Tags&language=en"
        response = requests.post(vision_url, headers=headers, data=image_data)
        data = response.json() #convert the response recieved to JSON format
        # print (data)       
        
    li = []
    for d in data['tags']:
        li.append(d['name'])
        
    print(li)
    cap = []
    count=0
    for i in li:
        count+=1
        if(count<4):
            dd = wikiquotes.get_quotes(i, "english")
            cap.append(dd[0])
    print(cap)

    tone_analyzer = ToneAnalyzerV3(
        username='09ad450e-eb00-4ef4-a6ab-e51093e505c4',
        password='kGnXm8HrMFWw',
    version='2017-09-26')

    for c in cap:
        utterances = [{'text': c, 'user': 'trailblazerr'}]    
        rtone=  tone_analyzer.tone_chat(utterances)
        #print(type(rtone))
        sent = rtone["utterances_tone"][0]["tones"][0]["tone_name"]
        # if(srtone["utterances_tone"][0]["tones"])
        
        
    client = textapi.Client(" 016eb657", " 590dff367360e75235f3753b78ef1488")
    sentiment = client.Hashtags({'text': cap[0]})
    hashtag = sentiment['hashtags']
    
    dictt = {}

    dictt = {"quotes" : cap , 
    "sent" : sent,
    "hashtag" : hashtag}
    print (dictt)

    return JsonResponse(dictt)








