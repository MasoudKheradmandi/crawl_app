code ="""
import requests
from bs4 import BeautifulSoup
my_list = []



def crawl():
    url = requests.get("https://codeexplore.ir/category/educational/")

    ins=BeautifulSoup(url.content, 'html')

    urls = ins.find_all('h3',class_="elementor-heading-title elementor-size-default")


    for url in urls:
        my_dic= {}
        my_dic["link"] = url.a["href"]
        my_dic["title"] = url.text
        my_list.append(my_dic)

    return my_list


crawl()
"""
index={}
exec(code,index)
print(index['my_list'])
