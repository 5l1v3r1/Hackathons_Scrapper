#Scraping the details of the hackathons in MLH



import requests
import bs4

res = requests.get('https://mlh.io/seasons/na-2019/events')
soup = bs4.BeautifulSoup(res.text,'lxml')

title = soup.select('h3')
startDate =soup.find_all('meta', {'itemprop': ['startDate']})
endDate =soup.find_all('meta', {'itemprop': ['endDate']})
links = soup.find_all('a', {'class': ['event-link']})
city = soup.find_all('span', {'itemprop': ['addressLocality']})
state = soup.find_all('span', {'itemprop': ['addressRegion']})


#for printing titles
i=0
c=0
while i < len(title):
    #if('[' not in title[i].text):  use for email protected hackathons 
    c+=1
    print(c, end ='')
    print(') '+ title[i].text)

    i+=1

#for printing links
i=0
c=0
while i < len(links):
    c+=1
    print(c, end ='')
    print(') '+ links[i].get('href'))

    i+=1

#for printing date
i=0
c=0
while i < len(startDate):
    c+=1
    print(c,end ='')
    print(') '+startDate[i].get('content')+'\t',end ='')
    print(endDate[i].get('content'))

    i+=1

#for printing city
i=0
c=0
while i < len(city):
    c+=1
    print(c, end ='')
    print(') '+ city[i].text)

    i+=1
#for printing state
i=0
c=0
while i < len(state):
    c+=1
    print(c, end ='')
    print(') '+ state[i].text)

    i+=1
#now getting to the official webpages of individual hackathon and getting the essential data
#i=0
#while i < len(links):
#    res = requests
