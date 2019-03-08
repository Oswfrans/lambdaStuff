#https://medium.com/@kagemusha_/scraping-on-a-schedule-with-aws-lambda-and-cloudwatch-caf65bc38848

Create new zip file to upload as lambda function, from the folder where your code is

create the s3 bucket.
create the IAM policy (bucket name needed)
Create IAM role (IAM policy needed)
Create lambda Function (IAM Role needed)
Create s3 bucket policy (lambda function name needed)
Verify the two emails in the SES service


IAM Policy :

{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "s3:PutObject",
                "s3:PutObjectAcl",
                "s3:PutObjectTagging",
                "s3:PutObjectVersionAcl",
                "s3:PutObjectVersionTagging"
                ],
        "Resource": [
            "arn:aws:s3:::flight-alerts"            #this is the s3 bucket
            ]
        },
        {
            "Effect":"Allow",
            "Action":["ses:*"],
            "Resource":"*"
        }
                ]
    
}

s3 bucket policy:

 {
"Id": "PolicyLambda",
"Version": "2012-10-17",
"Statement": [
{
  "Action": [
    "s3:PutObject",
    "s3:PutObjectAcl",
    "s3:PutObjectTagging",
    "s3:PutObjectVersionAcl",
    "s3:PutObjectVersionTagging"
  ],
  "Effect": "Allow",
  "Resource": "arn:aws:s3:::flight-alerts/*",
  "Principal": {
    "AWS": [
      "arn:aws:iam::149975319591:role/Lambda-Flights"   #lambda role arn
          ]
          }
        }
     ]
}