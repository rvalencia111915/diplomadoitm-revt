import boto3

rekognition = boto3.resource('rekognition', region_name='us-east-1', 
  aws_access_key_id='AKIAQWHCQCNBHE36CVXI',
  aws_secret_access_key='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')

respuesta = rekognition.detect_labels(Image={
  'S3Object': {
    'Bucket': 'bucket.juan.gomez',
    'Name': 'ejemplo.jpg'
  }},
  MaxLabels=5,
  MinConfidence=75)

for label in respuesta['Labels']:
  print(label['Name'],label['Confidence'])

                                                          