import sys
import urllib2
from bs4 import BeautifulSoup

toOpen = str(sys.argv[1])

def GetLinks(pageUrl, name_link):
  print("Running on " + pageUrl)
  soup = None
  try:
    url = urllib2.urlopen(pageUrl)
    html_page = url.read()
    soup = BeautifulSoup(html_page)
  except KeyboardInterrupt:
    sys.exit(0)
  except:
    return []

  toRet = []

  links = soup.find_all('a')
  for link in links:
    try:
      name = link.contents[0]
      fullLink = link.get('href')
      #print(fullLink)
      if not name in name_link:
        if not fullLink.startswith("http"):
          #print("Didn't start with http:")
          #print(pageUrl + fullLink)
          toRet.append(pageUrl + fullLink)
        else:
          #print("Started with http:")
          #print(fullLink)
          toRet.append(fullLink)
        
        #toRet.append(fullLink)
    except:
      continue

  return toRet

def PrintLinks(name_link):
  for link in name_link:
    print name_link[link]  

name_link = {}
toDoList = [sys.argv[1]]
doneList = []
curDepth = 0
while(len(toDoList) > 0):
  print("CurDepth = " + str(curDepth))
  newList = []
  GetLinks(toOpen, name_link)
  for link in toDoList:
    if(link in doneList):
      print("Skipping " + link)
      continue
    #print(link)
    else:
      tmpList = GetLinks(link, name_link)
    for item in tmpList:
      if(not item in newList):
        newList.append(item)
    doneList.append(link)
  toDoList = newList
  curDepth = curDepth + 1
  print("\n")
  print("todo: ")
  print(toDoList)
  print("\n")
  print("done: ")
  print(doneList)
  print("\n")
