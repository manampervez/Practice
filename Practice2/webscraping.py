import requests
from bs4 import BeautifulSoup
from bs4 import BeautifulSoup as bs
'''
import requests
from bs4 import BeautifulSoup

website= requests.get("https://pythonhow.com/example.html")
content1= website.content
print(content1)
soup=BeautifulSoup(content1,"html.parser")
all=soup.find_all("div",{"class":"cities"})
print(all)
#ok=all[0].find_all("h2")[0].text
#print(ok)



website= requests.get("http://www.aniyanetworks.net/contact/")
content1=website.content
soup=BeautifulSoup(content1,"html.parser")
all=soup.find_all("div",{"class":"vc_cta3-content"})
#print(all)
ok=all[0].find_all("h4")
print(ok)

'''

site = requests.get("http://www.aniyanetworks.net/contact")
soup = bs(site.content, "html.parser")
divs = soup.find_all("div", {"class": "vc_cta3-content"})
headers = [elem.find_all("h4") for elem in divs]
#print(dir(headers[0][0]))
print(headers[0][0].text)


