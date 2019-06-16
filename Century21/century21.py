import requests
from bs4 import BeautifulSoup

#r=requests.get("http://pyclass.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/")
headers = {'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'}
r = requests.get("http://www.pyclass.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/", headers=headers)
#r=requests.get("https://www.royallepage.ca/en/on/brampton/properties/")
c=r.content
soup=BeautifulSoup(c,"html.parser")
#print(soup.prettify())
all=soup.find_all("div",{"class":"propertyRow"})
all[0].find("h4",{"class":"propPrice"}).text.replace("\n","").replace(" ","")
#print(all)
#all2=all[0].find("h4",{"class":"propPrice"}).text.replace("\n","").replace(" ","")
#print(all2)

for item in all:
    print(item.find("h4",{"class","propPrice"}).text.replace("\n","").replace(" ",""))
    print(item.find_all("span",{"class","propAddressCollapse"})[0].text)
    print(item.find_all("span", {"class", "propAddressCollapse"})[1].text)

    try:
        print(item.find("span",{"class","infoBed"}).find("b").text)
    except:
        print(None)

    try:
        print(item.find("span",{"class","infoSqFt"}).find("b").text)
    except:
        print(None)

    try:
        print(item.find("span",{"class","infoValueFullBath"}).find("b").text)
    except:
        print(None)
    try:
        print(item.find("span",{"class","infoValueHalfBath"}).find("b").text)
    except:
        print(None)
    print(" ")
