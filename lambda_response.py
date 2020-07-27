import json
import boto3
import collections
import datetime
import time
# import paramiko

def lambda_handler(event, context):
    # TODO implement
    # print(event['detail'])
    # id = event['detail']['instance-id']
    
    # ec2 = boto3.resource('ec2')
    # # print(list(ec2.instances.filter(Filters=[{'Name': 'i-0feff7a5e1dacf109', 'Values': []}])))
    # client = boto3.client('ec2')
    
    # Associate IAM profile with EC2
    # response = client.associate_iam_instance_profile(
    #     IamInstanceProfile={
    #         'Arn': 'arn:aws:iam::177466765664:instance-profile/ManagedServices_Role',
    #         'Name': 'ManagedServices_Role'
    #     },
    #     InstanceId='i-090f980c8dfc5b9b8'
    # )
    
    # Add tags to EC2 instances
    # response = client.create_tags(Resources=['i-090f980c8dfc5b9b8'], 
    #     Tags=[{
    #         'Key':'test_lambda', 
    #         'Value':'True'
    #     }]
    # )
    
    # s3 = boto3.client('s3')
    # s3_client.download_file('YourBucketName','YourPEMFileObject.pem', '/tmp/keyname.pem')
    
    # "i-0feff7a5e1dacf109"
    # response = ec2.describe_instances()
    # for r in response['Reservations']:
    #     for i in r['Instances']:
    #         print(i['InstanceId'])
    #         print(i.keys())
    # instances = ec2.instances
    
    # for i in instances.all():
    #     for tag in i.tags:  # Get the name of the instance
    #         if tag['Key'] == 'Name':
    #             name = tag['Value']
    #             print(name)
    
    # Use SSM plugin for SSM info
    ssm = boto3.client('ssm')
    response = ssm.describe_instance_information(
        # Filters=[
        #     {
        #         'Key': 'string',
        #         'Values': [
        #             'string',
        #         ]
        #     },
        # ],
        # MaxResults=123,
        # NextToken='string'
    )
    print(response)
    
    success_mes = 'Successfully installed SSM agent on instance '
    return {
        'statusCode': 200,
        'body': json.dumps(success_mes)
    }


