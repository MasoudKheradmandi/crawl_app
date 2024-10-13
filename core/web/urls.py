from django.urls import path
from . import views


urlpatterns = [
    path('home/',views.home,name='home'),
    path('home-rss/',views.crawl_site_with_rss,name='home-rss'),

    path('website/',views.WebSiteApi.as_view(),name='website'),
]

