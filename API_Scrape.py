import urllib.request

# page is a reference to the page we want to open. You can change it if needed
print("Enter zip code")
zip = input()
page = urllib.request.urlopen(
    'http://api.openweathermap.org/data/2.5/weather?zip=' + zip + ',us&APPID=b5903c14117c998fc6ac94696db288d8')

for line in page:
    line = line.decode('utf-8')
    if 'temp' in line:
        where = line.find('temp')
        start = where + 6
        end = start + 5
        data = float(line[start:end])
        data = (data - 273.15) * (9 / 5) + 32
        print(data)
    if 'humidity' in line:
        where = line.find('humidity')
        start = where + 10
        end = start + 2
        data = line[start:end]
        print(data, '%')
    if 'pressure' in line:
        where = line.find('pressure')
        start = where + 10
        end = start + 2
        data = line[start:end]
        print(data, '%')


