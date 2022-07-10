import boto3
import botocore.exceptions

bucket_name = #バケット名を設定

key = 'notes.csv'

# リソース API を使用
resource = boto3.resource('s3')
bucket = resource.Bucket(bucket_name)


print(f'Start delete object {key}')

try:
    bucket.delete_objects(
        Delete={
            'Objects':[{
                'Key': key
            }]
        }
    )
except botocore.exceptions.ClientError as e:
    print(e)
    print('Delete object failed.')