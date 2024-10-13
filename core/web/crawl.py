from .models import WebSite

import requests
from bs4 import BeautifulSoup

def crawl_response():
    web=WebSite.objects.get(id=1)
    print('ss')
    m = web.code
    return exec(m)