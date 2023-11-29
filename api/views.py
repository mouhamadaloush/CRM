from django.shortcuts import render
from django.http import JsonResponse
import json
from website.models import Record
from django.forms.models import model_to_dict
from rest_framework.decorators import api_view
from rest_framework.response import Response
from website.serializers import RecordSerializer


# Create your views here.
def api_home(request, *args, **kwargs):
    data = {}
    try:
        data = json.loads(request.body)
    except:
        pass

    data["params"] = dict(request.GET)
    data["headers"] = dict(request.headers)
    data["content_type"] = request.content_type
    print(data["message"])
    return JsonResponse(data)

def get_record(request, *args, **kwargs):
    record = Record.objects.all().order_by("?").first()
    data = {}
    if record:
        data = model_to_dict(record)
    print(data)

    return JsonResponse(data)


@api_view(["GET", "POST"]) 
def rest_api1(request,*args, **kwargs):
    """
    REST API
    """
    record = Record.objects.all().order_by("?").first()
    data = {}
    if record:
        data = model_to_dict(record)

    return Response(data)

#using SERIALIZERS
@api_view(["GET"]) 
def get_rec(request,*args, **kwargs):
    """
    REST API
    """
    if kwargs:
        instance = Record.objects.get(id=kwargs['pk'])
    
    data = {}
    if instance:
        data = RecordSerializer(instance).data

    return Response(data)

@api_view(["POST"])
def add_rec(request,*args, **kwargs):
    serializer = RecordSerializer(data=request.data)
    data = {}
    if serializer.is_valid(raise_exception=True):
        instance=serializer.save()
        data = serializer.data
        print(data)
    else:
        print(serializer.is_valid())
    
    return Response(data)


@api_view(["POST"])
def del_rec(request,*args, **kwargs):
    data = {}
    if 'id' in dict(request.data).keys():
        try:
            Record.objects.get(id = int(request.data["id"])).delete()
            data["message"] = f"Record {request.data['id']} Deleted"
        except:
            data["message"] = f"!!!!!Record {request.data['id']} NOT EXISTED!!!!!"
    else:
        data["message"] = "YOU HAVE TO SEND AN ID"
    
    return Response(data)