import requests
import json
import csv
from datetime import datetime, timedelta
#this site is awesome!!
#https://curl.trillworks.com/

params = (
    ('appId', '0e0f7cfa'),
    ('appKey', '172bd1bcb9b1d822b99055a30985b21e'),
    ('requestedFields', 'airlineCode,flightNumber,city,currentTime,gate,remarks, remarksCode, scheduledTime, estimatedTime'),
    ('includeAirlines', 'QTR'),
    ('timeFormat', '24'),
    ('lateMinutes', '15'),
    ('useRunwayTimes', 'false'),
    ('excludeCargoOnlyFlights', 'false'),
)

#list of departure airports to include
airports = ['LHR', 'DXB'] #'LAX', 'DEN',
euAirports = []

requestList = []

for a in airports:
    curList = json.loads(requests.get("https://api.flightstats.com/flex/fids/rest/v1/json/"+a+"/departures" , params=params).text )["fidsData"]
    requestList = requestList + curList

toReportAlerts1 = len([z["flightNumber"] for z in requestList if z["remarksCode"]=="CANCELLED"])
toReportAlerts2 = len([z["flightNumber"] for z in requestList if z["remarksCode"]=="DEPARTURE_DELAYED"])

print(requestList)

fmt = '%H:%M'
def numHours(td):
    return td.seconds//3600

dep = [  numHours( datetime.strptime(z["estimatedTime"], fmt)- datetime.strptime(z["scheduledTime"] , fmt) ) for z in requestList
if 'estimatedTime' in z] #if z["airportCode"] in euAirports] #if z["remarksCode"]=="DEPARTURE_DELAYED"]
toReportAlerts3 = [ d for d in dep if d>3]

#print(dep)

#send email
#if toReportAlerts1>1 or toReportAlerts2>10 or toReportAlerts3>2 :
    #message code will go



#this is what we save to S3
#print(",".join(map(str, requestList)))


#so we push the requestList to an S3 bucket
#need to ask Zwelli what he wants to do with the alerts, for now we can assume email?


#import numpy as np
#np.savetxt("file_name.csv", np.column_stack((data1, data2)), delimiter=",", fmt='%s', header=header)


#lambda saving of data?
#https://stackoverflow.com/questions/44183216/aws-python-lambda-function-upload-file-to-s3
