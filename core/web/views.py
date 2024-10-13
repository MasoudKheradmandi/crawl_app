from django.shortcuts import render,HttpResponse
from django.db import IntegrityError
from .crawl import crawl_response
from .models import Post,WebSite


def home(request):
    data = crawl_response()
    webr=WebSite.objects.get(id=1)
    for web in data:
        Post.objects.get_or_create(website=webr,title=web['title'],post_link=web['link'])
    return HttpResponse("Done")