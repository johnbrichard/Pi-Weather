tempFile=open('temps.txt',"r")
humFile=open('hums.txt', "r")

temp = [int(x.strip()) for x in tempFile.readlines()]
hum = [int(x.strip()) for x in humFile.readlines()]
tempWeight=[(x/75) for x in temp]
humWeight=[(x/40) for x in hum]

totTemp=0
avgTemp=0
totHum=0
avgHum=0
count=0

for item in temp:
    totTemp+=temp[item]
    totHum+=hum[item]
    count+=1

print('Temp:',temp[count-1],'Weight:',round(tempWeight[count-1],2),'Hum:',hum[count-1],'Weight:',round(humWeight[count-1],2))

avgTemp=(totTemp/count)
avgHum=(totHum/count)

print('Average Temperature:',round(avgTemp,2),'Average Humidity:', round(avgHum,2))