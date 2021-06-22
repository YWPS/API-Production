import json

from django.http import JsonResponse, HttpResponse
from django.utils.crypto import get_random_string
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render

from .models import Image, Product, Item


@csrf_exempt
def CreateProduct(request, name):
    if request.method == "POST":
        # decode json
        jsonUnicode = request.body.decode('utf-8')
        jsonData = json.loads(jsonUnicode)
        # required fields
        items = jsonData["items"]
        username = jsonData["username"]
        # authenticate user
        user = username
        hash = get_random_string(length=40)
        # update or create model
        product = Product.objects.update_or_create(
            user=user, name=name, hash=hash)

        for item in items:
            Item.objects.update_or_create(
                name=item["name"], code=item["code"], product=product[0])
        # response
        return JsonResponse({
            "url": f"https://api.qrserver.com/v1/create-qr-code/?data={hash}?size=1024*1024",
            "hash": f"{hash}"
        })


def GetProduct(request, hash):
    target = Product.objects.get(hash=hash)
    code = []
    for item in target.items.all():
        code.append({"name": item.name, "code": item.code})

    return JsonResponse({
        "name": target.name,
        "user": target.user,
        "code": code

    })


def SearchProduct(request, query):

    res = []
    target = Product.objects.filter(name__icontains=query)

    for item in target:
        res.append({
            "name": item.name,
            "user": item.user,
            "hash": item.hash
        })
    return JsonResponse(res, safe=False)


@csrf_exempt
def UploadImage(request, hash):
    if request.method == "POST":
        # decode json
        jsonUnicode = request.body.decode('utf-8')
        jsonData = json.loads(jsonUnicode)
        # required fields
        extension = jsonData['extension']
        full = jsonData['full']
        Image.objects.update_or_create(
            hash=hash, extension=extension, full=full)
        # response
        return HttpResponse('', status=200)
    return render(request, 'upload.html', {
        "hash": hash
    })


def DisplayImage(request, hash):
    try:
        target = Image.objects.get(hash=hash)
        return render(request, 'display.html', {
            "full": target.full
        })
    except:
        return HttpResponse("<h1>沒有上載圖片</h1>")
