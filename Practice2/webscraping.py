import requests
from bs4 import beautifulsoup

website= requests.get("https://pythonhow.com/example.html")
content1=website.content