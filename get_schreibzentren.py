# Webcrawler
# Version 0.1
# Author: Christopher Klamm
# 11.3.2017

#import urllib2
import urllib.request
from bs4 import BeautifulSoup
import geocoder
import csv


grippe = "http://www.schreibwerkstatt.uni-stuttgart.de/wir-ueber-uns/Vernetzung/Schreibzentren_im_deutschsprachigen_Raum.html"
#page = urllib2.urlopen(grippe)
page = urllib.request.urlopen('http://www.schreibwerkstatt.uni-stuttgart.de/wir-ueber-uns/Vernetzung/Schreibzentren_im_deutschsprachigen_Raum.html')
soup = BeautifulSoup(page, "lxml")

data = []
all_news = soup.find("table", { "class" : "belted" })
table = all_news
table_body = table.find('tbody')
rows = table_body.find_all('tr')

i = 0
for row in rows:
    cols = row.find_all('td')
    articles = {i.a['href']: i.text.strip() for i in cols if i.a}
    #print(articles.keys())
    cols = [ele.text.strip() for ele in cols]
    data.append([ele for ele in cols if ele] + list(articles.keys()) + list(geocoder.google(cols[1]).latlng))

writer = csv.writer(open("writing_center.csv", "w"))
writer.writerow(["City", "SchoolName", "Typ", "Url", "GeoLat", "GeoLng"])
writer.writerows(data)

#gesamt = []

#for d in data:
#	gesamt.append([d[1], d[2], geocoder.google(d[0]).latlng])


#for g in gesamt:
#	print(g)

#g = geocoder.google('Darmstadt')
#print(g.latlng)

#articles = {i.a['href']: i.text.strip() for i in all_news if i.a}
#articles = all_news
#for article in articles:
	#s = '{title}: {url}: {date}'.format(title=articles[article],url='https://de.grippenet.ch/de/'+article, date=article[:10])
	#title = articles[article]
#	url = article
#	print(url)