import requests
import urllib.request as url
from PIL import Image

#country = input("Please input country name ")
country = 'Spain'
#api request for the target country info
infoGet = requests.get('https://restcountries.eu/rest/v2/name/'+country)
test = infoGet.json()
print(test)

print("\n\n")
print("\n\n")
num=2
#api request for the target country photos
photoGet = requests.get('https://api.unsplash.com/photos/random?count=1&client_id=RgR2GJQYV5BJVkIGvw2RuC5S7txQADAYTVQo-JjO560&query='+country)
data = photoGet.json()
print(data)
rawPhoLoc=data[0]['urls']['raw']
regPhoLoc=data[0]['urls']['regular']
print("\n\n")
print('pic'+str(num)+'.jpg'+"\n")
url.urlretrieve(rawPhoLoc, 'pic'+str(num)+'.jpg')
url.urlretrieve(regPhoLoc, 'pic'+str(num+1)+'.jpg')
#url.urlretrieve(rawPhoLoc, 'pic'+num+'.jpg')
#print("\n"+rawPhoLoc)
#stores city name of photo
cityName=data[0]['location']['city']
print(cityName)