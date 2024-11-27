import boto3

dynamodb = boto3.resource('dynamodb', region_name='us-east-1', 
  aws_access_key_id='AKIAQWHCQCNBHE36CVXI',
  aws_secret_access_key='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')

tabla = dynamodb.Table('tabla-estivenvalencia')

respuesta = tabla.delete_item(Key={id: '1'})

print("Elemento eliminado exitosamente")

      