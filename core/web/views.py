from django.shortcuts import render,HttpResponse
from rest_framework.views import APIView
from rest_framework import serializers,status
from django.db import IntegrityError
from rest_framework.response import Response
from .crawl import crawl_response
from .rss import crawl_rss
from .models import Post,WebSite


def home(request):
    data = crawl_response()
    webr=WebSite.objects.get(id=1)
    for web in data:
        Post.objects.get_or_create(website=webr,title=web['title'],post_link=web['link'])
    return HttpResponse("Done")

def crawl_site_with_rss(request):
    website = WebSite.objects.get(crawl_strategies="rss",id=1)
    data_set =  crawl_rss(website)
    for data in data_set:
        Post.objects.get_or_create(website=website,title=data['title'],post_link=data['link'])
    return HttpResponse("Done RSS")


class WebSiteApi(APIView):

    class WebSiteSerializer(serializers.ModelSerializer):
        class Meta:
            model = WebSite
            fields = "__all__"
    
    def get(self,request):
        our_web = WebSite.objects.filter(status=True)
        serializer = self.WebSiteSerializer(our_web,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
