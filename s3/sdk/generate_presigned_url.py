import boto3
import botocore.exceptions

bucket_name = #バケット名を設定
key = 'notes.csv'
print(f'Generate presigned url for {key}')

# クライアント API を使用
client = boto3.client('s3')

# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Client.generate_presigned_url
try:
    url = client.generate_presigned_url(
        ClientMethod='get_object',
        Params={'Bucket': bucket_name, 'Key': key},
        ExpiresIn=3600,
        HttpMethod='GET'
    )
    print(url)
except botocore.exceptions.ClientError as e:
    print(e)
    print('Generate url failed.')
