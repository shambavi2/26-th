from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
# Create your views here.
def insert_topic(request):
    tn=input('enter topic name')
    T=Topic.objects.get_or_create(Topic_name=tn)[0]
    T.save()
    return HttpResponse('topic is inserted successfully')


def insert_Webpage(request):
    tn=input('enter topic_name')
    name=input('enter a name')
    url=input('enter url')
    T=Topic.objects.get_or_create(Topic_name=tn)[0]
    T.save()
    W=Webpage.objects.get_or_create(Topic_name=T,name=name,url=url)[0]
    W.save()
    return HttpResponse('web page data inserted successfully')

def insert_Access_Records(request):
    tn=input('enter topic name')
    name=input('enter name')
    url=input('enter url')
    date=input('enter date')
    T=Topic.objects.get_or_create(Topic_name=tn)[0]
    T.save()
    W=Webpage.objects.get_or_create(Topic_name=T,name=name,url=url)[0]
    W.save()
    A=Access_Record.objects.get_or_create(name=W,date=date)[0]
    A.save()
    return HttpResponse('access record data inserted successfully')

    

