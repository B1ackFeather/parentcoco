from django.shortcuts import render
from django.http import HttpResponse
import pymongo
import json
db = pymongo.database.Database(pymongo.MongoClient(), 'parentcoco')


def hello(request):

    return HttpResponse("Hello world ! ")
# Create your views here.


def login(request):
    parent = db.get_collection("parent")
    parentID = request.GET.get("ID")
    password = request.GET.get("password")
    ls = parent.find_one({'parentID': parentID, 'password': password})
    if ls:
        return HttpResponse(json.dumps({'status': 'True'}))
    else:
        return HttpResponse(json.dumps({'status': 'False'}))
