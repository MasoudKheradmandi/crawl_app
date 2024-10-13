from django.urls import path
from . import views


urlpatterns = [
    path('home/',views.home,name='home'),
    path('website/',views.WebSiteApi.as_view(),name='website'),
]

