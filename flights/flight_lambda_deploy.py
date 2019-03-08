#do I need this?
#Handler: index.lambda_handler
#python: 3.6

import boto3
import datetime 
import requests
import json
import csv

#this is the structure for the actual lambda function
def lambda_handler(event, context):
    #here we will paste the request code



    if toReportAlerts1>1 or toReportAlerts2>10 or toReportAlerts3>2 :
        #email code
        SENDER = "AWS Flight Alerts <o.frans@payvision.com>" #should change this later
        # If your account is still in the sandbox, this address must be verified.
        RECIPIENT = "risk@payvision.com"
        AWS_REGION = "eu-west-2" #change to frankfurt

        # The subject line for the email.
        SUBJECT = "AWS Flight Alerts"

        BODY_TEXT = ("For" + str(Airline) + "there are" + str(toReportAlerts1) 
                    + "cancelled flights this hour. Moreover, the amount of delayed flights" + str(toReportAlerts2)
                    + "the amount of flights in the EU delayed more than 3 hours are" + Str(toReportAlerts3)
                    )

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

    #saving to s3
    string = ",".join(map(str, requestList))
    encoded_string = string.encode("utf-8")

    cur_dt = datetime.datetime.today().strftime('%Y%m%d')
    currentTime = datetime.datetime.today().strftime('%H%Y%m%d')

    #do I have these? I will need to change them
    #$ACCESS_KEY_ID = 'Abcdefg'
    #ACCESS_SECRET_KEY = 'hijklmnop+6dKeiAByFluK1R7rngF'

    bucket_name = "Flights"
    file_name = str(currentTime)+".txt"
    lambda_path = "/tmp/" + file_name

    s3_path = "/qtr/"+str(cur_dt)+"/" + file_name

    s3 = boto3.resource("s3" ,
                aws_access_key_id=ACCESS_KEY_ID,
                aws_secret_access_key=ACCESS_SECRET_KEY,)
    s3.Bucket(bucket_name).put_object(Key=s3_path, Body=encoded_string)