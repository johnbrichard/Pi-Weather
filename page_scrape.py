import urllib.request
import re

page=urllib.request.urlopen('http://ftp.jamesbraman.com/weather/Mike_log.txt')

for line in page:

    line=line.decode('utf-8') #removes the b literals
    if "Humidity" in line:
        print(re.findall('\d+',line))





