import urllib.request
import io
from bs4 import BeautifulSoup

for i in range(25, 32):
    url = "https://www.yr.no/sted/Norge/Aust-Agder/Grimstad/Grimstad/almanakk.html?dato="
    dato ="2015-05-"
    dato += str(i)
    url += dato
    filename = dato + ".csv"

    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page, "html.parser")
    text = open(filename, "w")
    text.write("klokke:tempmålt:tempmax:tempmin:nedbør:vind:Luft \n")
    x = soup.find_all("tr")

    for i in range(0,len(x)):
        if i > 7:
            temprature = x[i].find_all('td' ,{"class" : "temperature plus"})
            klokke = x[i].find_all('strong')
            regn = x[i].find_all('td')[4:5]
            vind = x[i].find_all('td')[6:7]
            fukt = x[i].find_all('td')[7:8]
            for s in klokke:
                text.write(str(s.contents[0])[3:].replace(",","."))
                text.write(":")
            for t in temprature:
                text.write(str(t.contents[0])[:-1].replace(",","."))
                text.write(":")
            for r in regn:
                text.write(str(r.contents[0])[:-2].replace(",","."))
                text.write(":")
            for v in vind:
                text.write(str(v.contents[0])[:-3].replace(",","."))
                text.write(":")
            for f in fukt:
                text.write(str(f.contents[0])[:-1].replace(",","."))
            text.write("\n")
    text.close()

