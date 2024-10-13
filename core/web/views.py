from django.shortcuts import render
from .crawl import crawl_response
from .models import Post


def home(request):
    x = crawl_response()

    # Post.objects.create(website=1,title=)