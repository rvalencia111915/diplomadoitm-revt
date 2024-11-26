import boto3

dynamodb = boto3.resource('dynamodb', region_name='us-east-1', 
  aws_access_key_id='AKIAQWHCQCNBHE36CVXI',
  aws_secret_access_key='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')

tabla = dynamodb.Table('tabla-estivenvalencia')

respuesta = tabla.put_item(
  Item={
    'id': '1',
    'nombre': 'Estiven Valencia',
    'edad': '34',
    'ciudad': 'Medellín'
  }
)

print("Proceso exitoso")