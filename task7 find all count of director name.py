from task1 import top_movies
import requests
from bs4 import BeautifulSoup
import json
h=[]
def  analyse_movies_director(top_movies):
    for i in range(0,250):
        a=top_movies[i]["link"]
        d1={}
        page=requests.get(a)
        soup=BeautifulSoup(page.text,'html.parser')
        director=soup.find("a",class_="ipc-metadata-list-item__list-content-item ipc-metadata-list-item__list-content-item--link").get_text()
        d1["Director"]=director
        h.append(d1)
    print(h)
    k=[]
    f=[]
    s={}
    for u in h:
        for j in u:
            if u[j] not in k:
                k.append(u[j])
        f.append(u[j])
    for j in range(len(k)):
        c=0
        for z in range(len(f)):
            if k[j]==f[z]:
                c=c+1
                s[k[j]]=c
    return s
gg=analyse_movies_director(top_movies)
with open("task7.json","w")as rr:
    json.dump(gg,rr,indent=2)

    