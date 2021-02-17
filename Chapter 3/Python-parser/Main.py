import os
import requests
from bs4 import BeautifulSoup as bs

os.system("cls")

urlStr = "https://tw.yahoo.com/?guccounter=1"

true = True
false = False
null = None

def getHTML_FromURL(urlStr):
    connection = requests.get(urlStr)
    return connection.text if (connection.status_code == 200) else ""

def getNewsTitles(html):
    titles = {}

    # No need to worry about any future changes of the news' class
    aTags = html.find_all("a", href = true)
    for a in aTags:
        href = a["href"]
        if (href == null):
            continue
        if ("tw.news.yahoo.com" in href and href.endswith(".html")):
            title = a.string
            if (title == null):
                continue
            titles[title] = href
    
    return titles

# End of functions

html = getHTML_FromURL(urlStr)
if (html == ""):
    print("Unable to get HTML.")
    exit

print("Got HTML from URL successfully.")

html = bs(html, "html.parser")

titles = getNewsTitles(html)
# print(titles)

for k, v in titles.items():
    print(k + " (" + v + ")")