import urllib.request

page=urllib.request.urlopen('http://ftp.jamesbraman.com/weather/Mike_log.txt')

code=page.read()

print(code)
