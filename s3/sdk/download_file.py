import boto3
import botocore.exceptions

bucket_name = #バケット名を設定

key = 'notes.csv'
file_name = './notes_download.csv'

# リソース API を使用
resource = boto3.resource('s3')
bucket = resource.Bucket(bucket_name)


print(f'Start get object {key}')

try:
    bucket.download_file(key, file_name)
except botocore.exceptions.ClientError as e:
    print(e)
    print('Bucket creation failed.')