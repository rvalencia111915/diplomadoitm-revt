import boto3

s3 = boto3.client(
  's3', 
  aws_access_key_id='AKIAQWHCQCNBHE36CVXI',
  aws_secret_access_key='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')

resultado = s3.list_buckets()

for bucket in resultado['Buckets']:
  print(bucket['Name'])