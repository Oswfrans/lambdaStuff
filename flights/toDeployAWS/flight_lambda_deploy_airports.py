import boto3
from botocore.exceptions import ClientError
from datetime import datetime, timedelta
import requests
import json

#this is the structure for the actual lambda function
def lambda_handler(event, context):
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
        toReportAlerts1 = len([z["flightNumber"] for z in requestList if z["remarksCode"]=="CANCELLED" and z["airlineCode"]==r ])
        toReportAlerts2 = len([z["flightNumber"] for z in requestList if z["remarksCode"]=="DEPARTURE_DELAYED" and z["airlineCode"]==r ])
        fmt = '%H:%M'
        dep = [  numHours( datetime.strptime(z["estimatedTime"], fmt)- datetime.strptime(z["scheduledTime"] , fmt) ) for z in requestList
        if 'estimatedTime' in z and z["airportCode"] in euAirports and z["airlineCode"]==r] 
        toReportAlerts3 = len([ d for d in dep if d>3])

        if toReportAlerts1>1 or toReportAlerts2>10 or toReportAlerts3>2 :
            message.append(str(r)+" has the following alerts. There are " + str(toReportAlerts1) 
                        + " cancelled flights this hour. Moreover, the amount of delayed flights is " + str(toReportAlerts2)
                        + " the amount of flights in the EU delayed more than 3 hours are " + str(toReportAlerts3) +" \n")
        
    #you also need to iterate over the keys of the dict
    for k in requestDict.keys():
        toReportAlertsAirport1 = len([z["flightNumber"] for z in requestDict[k] if z["remarksCode"]=="CANCELLED"])
        toReportAlertsAirport2 = len([z["flightNumber"] for z in requestDict[k] if z["remarksCode"]=="DEPARTURE_DELAYED"])
        
        if toReportAlerts1>5 or toReportAlerts2>10:
            message.append(str(k)+" has the following alerts. There are " + str(toReportAlerts1) 
                        + " cancelled flights this hour. Moreover, the amount of delayed flights is " + str(toReportAlerts2) +" \n")
    
    #saving to s3
    stringToKeep = ','.join((map(str, requestList)))
    encoded_string = stringToKeep.encode("utf-8")

    cur_dt = datetime.today().strftime('%Y%m%d')
    currentTime = datetime.today().strftime('%H%Y%m%d')    
    #cur_dt = datetime.datetime.today().strftime('%Y%m%d')
    #currentTime = datetime.datetime.today().strftime('%H%Y%m%d')

    #do I have these? I will need to change them
    #$ACCESS_KEY_ID = 'Abcdefg'
    #ACCESS_SECRET_KEY = 'hijklmnop+6dKeiAByFluK1R7rngF'

    bucket_name = "flight-alerts"
    file_name = str(currentTime)+".txt"
    lambda_path = "/tmp/" + file_name

    s3_path = "data/qtr/"+str(cur_dt)+"/" + file_name

    s3 = boto3.resource("s3" , )
                #aws_access_key_id=ACCESS_KEY_ID,
                #aws_secret_access_key=ACCESS_SECRET_KEY,)
    s3.Bucket(bucket_name).put_object(Key=s3_path, Body=encoded_string)

    #send email regardless, this can be conditional
    #if ( ",".join(map(str, message)) ):
    #email code
    SENDER = "AWS Flight Alerts <o.frans@payvision.com>" #should change this later
    # If your account is still in the sandbox, this address must be verified.
    RECIPIENT = "oswfrans@gmail.com"
    AWS_REGION = "eu-west-1" #change to frankfurt or not? Currently Ireland where SES is

    # The subject line for the email.
    SUBJECT = "AWS Flight Alerts"

    #test this line
    BODY_TEXT = ( ",".join(map(str, message)) )

    CHARSET = "UTF-8"

    client = boto3.client('ses',region_name=AWS_REGION)

    # Try to send the email.
    try:
        #Provide the contents of the email.
        response = client.send_email(
            Destination={
                'ToAddresses': [
                    RECIPIENT,
                ],
            },
            Message={
                'Body': {
                    'Text': {
                        'Charset': CHARSET,
                        'Data': BODY_TEXT,
                    },
                },
                'Subject': {
                    'Charset': CHARSET,
                    'Data': SUBJECT,
                },
            },
            Source=SENDER,
        )
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        print("Email sent! Message ID:"),
        print(response['MessageId'])
        
    return 1