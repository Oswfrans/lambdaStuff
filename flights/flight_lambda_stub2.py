from datetime import datetime, timedelta
import requests
import json
import csv

#here we will paste the request code
params = (
    ('appId', '0e0f7cfa'),
    ('appKey', '172bd1bcb9b1d822b99055a30985b21e'),
    ('requestedFields', 'airlineCode,flightNumber,city,currentTime,gate,remarks, remarksCode, scheduledTime, estimatedTime'),
    ('timeFormat', '24'),
    ('lateMinutes', '15'),
    ('useRunwayTimes', 'false'),
    ('excludeCargoOnlyFlights', 'false'),
)

#list of departure airports to include
airports = ['LHR', 'DXB'] #'LAX', 'DEN',
euAirports = []
#list of airlines
airlines = ['QR'] 

requestList = []
requestDict= {}

for a in airports:
    curList = json.loads(requests.get("https://api.flightstats.com/flex/fids/rest/v1/json/"+a+"/departures" , params=params).text )["fidsData"]
    requestList = requestList + curList

    requestDict[a] = curList

#why not store in a list what we want to sent, so we can send one email?
message=[]
def numHours(td):
    return td.seconds//3600

#so than you iterate over the airlines
for r in airlines:
    toReportAlerts1 = len([z["flightNumber"] for z in requestList if z["remarksCode"]=="CANCELLED" and z["airlineCode"]==r])
    toReportAlerts2 = len([z["flightNumber"] for z in requestList if z["remarksCode"]=="DEPARTURE_DELAYED" and z["airlineCode"]==r])
    fmt = '%H:%M'
    dep = [  numHours( datetime.strptime(z["estimatedTime"], fmt)- datetime.strptime(z["scheduledTime"] , fmt) ) for z in requestList
    if 'estimatedTime' in z and z["airportCode"] in euAirports and z["airlineCode"]==r] 
    toReportAlerts3 = len([ d for d in dep if d>3])

    #if toReportAlerts1>1 or toReportAlerts2>10 or toReportAlerts3>2 :
    message.append(str(r)+"has the following alerts. There are " + str(toReportAlerts1) 
                + " cancelled flights this hour. Moreover, the amount of delayed flights is " + str(toReportAlerts2)
                + " the amount of flights in the EU delayed more than 3 hours are " + str(toReportAlerts3) +" \n")

#you also need to iterate over the keys of the dict
for k in requestDict.keys():
    print(k)
    toReportAlertsAirport1 = len([z["flightNumber"] for z in requestDict[k] if z["remarksCode"]=="CANCELLED"])
    toReportAlertsAirport2 = len([z["flightNumber"] for z in requestDict[k] if z["remarksCode"]=="DEPARTURE_DELAYED"])
    
    #if toReportAlerts1>5 or toReportAlerts2>10:
    message.append(str(k)+"has the following alerts. There are " + str(toReportAlerts1) 
                + " cancelled flights this hour. Moreover, the amount of delayed flights is " + str(toReportAlerts2) +"\n")

print(message)    