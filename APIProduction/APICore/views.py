import json

from django.http import JsonResponse
from django.http.response import HttpResponse
from django.utils.crypto import get_random_string
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render

from .models import Image, Product


@csrf_exempt
def CreateProduct(request, name):
    if request.method == "POST":
        # decode json
        jsonUnicode = request.body.decode('utf-8')
        jsonData = json.loads(jsonUnicode)
        # required fields
        code1code = jsonData["code1code"]
        code2code = jsonData["code2code"]
        code3code = jsonData["code3code"]
        code1name = jsonData["code1name"]
        code2name = jsonData["code2name"]
        code3name = jsonData["code3name"]
        username = jsonData["username"]
        # authenticate user
        user = username
        hash = get_random_string(length=40)
        # update or create model
        Product.objects.update_or_create(
            user=user, name=name, hash=hash, code1code=code1code, code2code=code2code, code3code=code3code, code1name=code1name, code2name=code2name, code3name=code3name)

        # response
        return JsonResponse({
            "url": f"https://api.qrserver.com/v1/create-qr-code/?data={hash}?size=1024*1024"
        })


@csrf_exempt
def GetProduct(request, hash):
    target = Product.objects.get(hash=hash)
    return JsonResponse({
        'name': target.name,
        "code1name": target.code1name,
        "code1code": target.code1code,
        "code2name": target.code2name,
        "code2code": target.code2code,
        "code3name": target.code3name,
        "code3code": target.code3code,
        'user': target.user
    })


@csrf_exempt
def UploadImage(request, name):
    if request.method == "POST":
        # decode json
        jsonUnicode = request.body.decode('utf-8')
        jsonData = json.loads(jsonUnicode)
        # required fields
        extension = jsonData['extension']
        full = jsonData['full']
        Image.objects.update_or_create(
            name=name, extension=extension, full=full)
        # response
        return HttpResponse('', status=200)
    return render(request, 'upload.html', {
        "name": name
    })


def DisplayImage(request, name):
    target = Image.objects.get(name=name)
    return render(request, 'display.html', {
        "full": target.full
    })
