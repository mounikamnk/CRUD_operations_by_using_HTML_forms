from django.shortcuts import render
from django.http import HttpResponse
from app.models import *
# Create your views here.
def first(request):
    if request.method=='POST':
        username=request.POST['un']
        password=request.POST['pw']
        print(username)
        print(password)
        return HttpResponse('data is submited')
    return render(request,'first.html')

def insert_topic(request):
    if request.method=='POST':
        topic=request.POST['tn']
        TO=Topic.objects.get_or_create(topic_name=topic)[0]
        TO.save()
        return HttpResponse('insertion of topic is done')

    return render(request,'insert_topic.html')


def insert_webpage(request):
    LTO=Topic.objects.all()
    d={'LTO':LTO}
    if request.method=='POST':
        topic=request.POST['top']
        name=request.POST['name']
        url=request.POST['url']
        TO=Topic.objects.get(topic_name=topic)
        WO=Webpage.objects.get_or_create(topic_name=TO,name=name,url=url)[0]
        WO.save()
        return HttpResponse('insertion of webpage is done')
    return render(request,'insert_webpage.html',d)

def insert_accessrecord(request):
    if request.method=='POST':
        name=request.POST['name']
        WO=Webpage.objects.get(name=name)
        date=request.POST['date']
        author=request.POST['author']
        AO=AccessRecord.objects.get_or_create(name=WO,date=date,author=author)[0]
        AO.save()
        return HttpResponse('insertion of accessrecord is done')
    return render(request,'insert_accessrecord.html')
def retrive_webpage(request):
    LTO=Topic.objects.all()
    d={'LTO':LTO}
    if request.method=='POST':
        MSTS=request.POST.getlist('topic')
        RWOS=Webpage.objects.none()

        for i in MSTS:
            RWOS=RWOS|Webpage.objects.filter(topic_name=i)
        d1={'RWOS':RWOS}
        return render(request,'disply_webpage.html',d1)
    return render(request,'retrive_webpage.html',d)



def retrive_accessrecord(request):
    WTO=Webpage.objects.all()
    d={'WTO':WTO}
    if request.method=='POST':
        MSWS=request.POST.getlist('name')
        RAOS=AccessRecord.objects.none()

        for i in MSWS:
            RAOS=RAOS|AccessRecord.objects.filter(id=i)
        d1={'RAOS':RAOS}
        return render(request,'disply_accessrecord.html',d1)
    return render(request,'retrive_accessrecord.html',d)
    


def checkbox(request):
    LTO=Topic.objects.all()
    d={'LTO':LTO}
    return render(request,'checkbox.html',d)
