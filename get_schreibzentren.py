# Webcrawler for writing centre in germany, austria and switzerland
# Version 0.2
# Author: Chkla
# 29.3.2017

import urllib.request
from bs4 import BeautifulSoup
import geocoder
import csv

# open the url e.g. schreibwerkstatt.uni-stuttgart.de
page = urllib.request.urlopen('http://www.schreibwerkstatt.uni-stuttgart.de/wir-ueber-uns/Vernetzung/Schreibzentren_im_deutschsprachigen_Raum.html')
soup = BeautifulSoup(page, "lxml")

# list to save schoolname, typ, link and the coordinates of each entitiy
data = []

# select just the table
table = soup.find("table", { "class" : "belted" })
table_body = table.find('tbody')
rows = table_body.find_all('tr')

# interate through all rows
for row in rows:
	# select one row
    cols = row.find_all('td')

    # get the link
    articles = {i.a['href']: i.text.strip() for i in cols if i.a}

    # get the text
    cols = [ele.text.strip() for ele in cols]

    # add schoolname, typ, link and the coordinates of each entitiy to the list
    data.append([ele for ele in cols if ele] + list(articles.keys()) + list(geocoder.google(cols[1]).latlng))

# open/ creat a new csv file
writer = csv.writer(open("writing_center.csv", "w"))
# specify the rows
writer.writerow(["City", "SchoolName", "Typ", "Url", "GeoLat", "GeoLng"])

# save all data
writer.writerows(data)