import boto3
#AWS_REGIONS=["us-east-1","us-east-2"]

def ec2_state():
  AWS_REGIONS=["us-east-1","us-east-2"]
  for AWS_REGION in AWS_REGIONS:
    EC2_RESOURCE = boto3.resource('ec2', region_name=AWS_REGION)
    sum=0
    instances = EC2_RESOURCE.instances.all()
    print(f'Region-"{AWS_REGION}":')
    for instance in instances:
      print(f'EC2 instance {instance.id}" information:')
      print(f'Instance state: {instance.state["Name"]}')
      print(f'Instance AMI: {instance.image.id}')
      print(f'Instance platform: {instance.platform}')
      print(f'Instance type: "{instance.instance_type}')
      print(f'Piblic IPv4 address: {instance.public_ip_address}')
      print('-'*60)
      sum=sum+1
    print(f'\nTotal Number of Instance running "{sum}"\n')

def list_bkt_obj():
  profile = str("default")
  olddate = str("2021-12-04")
  smallbucketsize = int(10)
  emptybucketlist=""
  oldbucketlist=""
  smallbucketlist=""
  AWS_REGION = "us-east-2"

  client = boto3.client("s3", region_name=AWS_REGION)
  response = client.list_buckets()
  s3_resource = boto3.resource("s3", region_name=AWS_REGION)
  print("Listing Amazon S3 Buckets:")
  for bucket in response['Buckets']:
    print(f"{bucket['Name']}\n")
    print("Listing Amazon S3 Bucket objects/files:")
    S3_BUCKET_NAME = f"{bucket['Name']}"
    print(S3_BUCKET_NAME)
    s3_bucket = s3_resource.Bucket(S3_BUCKET_NAME)
    for obj in s3_bucket.objects.all():
         print(f'-- {obj.key}')
         
def total_bucket():
  s3 = boto3.client("s3")
  response = s3.list_buckets()
  s3_resource = boto3.resource("s3")
  sum=0
  print("Bucket List:")
  for bucket in response['Buckets']:
    print(f'{bucket["Name"]}')
    S3_BUCKET_NAME = f"{bucket['Name']}"
    print(S3_BUCKET_NAME)
    sum=sum+1
  print(f'\nTotal number of s3 bucket "{sum}"')
  
def list_account():
#client = boto3.client(profile_name='devadmin')
  client = boto3.client('organizations', aws_access_key_id='AKIAS3UIATCRHGRCPJ7R', aws_secret_access_key='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')
  response = client.list_accounts()
  Accounts = response['Accounts']
  sum=0
  for Account in Accounts:
    print(Account)
    sum=sum+1
  print(f'\n==> Total Number of AWS Account: "{sum}"\n')
    
def total_lambda():
  AWS_REGIONS=["us-east-1","us-east-2"]
  for AWS_REGION in AWS_REGIONS:
    client = boto3.client('lambda',region_name=AWS_REGION)
    sum=0
    response = client.list_functions(
      FunctionVersion="ALL"
    )
    functions = response['Functions']
    print(f'Region-"{AWS_REGION}":\n')
    print(f'Lambda Function List:')
    for function in functions:  
      print(function ["FunctionName"])
      sum=sum+1
    print(f'\n==> Total Number function in region-"{AWS_REGION}": "{sum}"\n')
    
def list_used_resource():
  AWS_REGIONS=["us-east-1","us-east-2"]
  for AWS_REGION in AWS_REGIONS:
    client = boto3.client('resourcegroupstaggingapi', region_name=AWS_REGION)
    paginator = client.get_paginator('get_resources')
    page_iterator = paginator.paginate()
    print(f'Resource List:\n')
    for page in page_iterator:        
      for acct in page['ResourceTagMappingList']:
        print(acct['ResourceARN'])
        
def ec2_running_state():
  AWS_REGIONS=["us-east-1","us-east-2"]
  INSTANCE_STATE = 'running'
  for AWS_REGION in AWS_REGIONS:
    EC2_RESOURCE = boto3.resource('ec2', region_name=AWS_REGION)
    sum=0
    instances = EC2_RESOURCE.instances.filter(
      Filters=[
        {
            'Name': 'instance-state-name',
            'Values': [
                INSTANCE_STATE
            ]
        }
      ]
    )

    print(f'Instances in state "{INSTANCE_STATE}" in region-"{AWS_REGION}":')

    for instance in instances:
      print(f'  - Instance ID: {instance.id}')
      sum=sum+1
    
    print(f'\nTotal Number of Instance running "{sum}"\n')    