import boto3
import botocore.exceptions


bucket_name = #バケット名を設定
print(f'Start delete bucket {bucket_name}')

# リソース API を使用
resource = boto3.resource('s3')
bucket = resource.Bucket(bucket_name)

try:
    bucket.delete()

    waiter = resource.meta.client.get_waiter('bucket_not_exists')
    waiter.wait(Bucket=bucket_name)

    print('Bucket deleted.')
except botocore.exceptions.ClientError as e:
    print(e)
    print('Delete bucket failed.')