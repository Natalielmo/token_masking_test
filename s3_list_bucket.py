import boto3
session = boto3.Session(
    aws_access_key_id='AKIAIOSFODNN7EXAMPLE',
    aws_secret_access_key='wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY',
)

s3 = session.resource('s3')

my_bucket = s3.Bucket('bucket_name')

for file in my_bucket.objects.all():
    print(file.key)
