import boto3
import botocore.exceptions

import os

bucket_name = #バケット名を設定

file_name = ''
pairdir = os.path.dirname(__file__)
file_path = os.path.join(pairdir, file_name)
print(f'Start upload file {file_path}')

# リソース API を使用
resource = boto3.resource('s3')
bucket = resource.Bucket(bucket_name)

try:
    bucket.upload_file(file_path, file_path)
except botocore.exceptions.ClientError as e:
    print(e)
    print('File upload failed.')
