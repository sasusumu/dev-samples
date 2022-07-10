import boto3
import botocore.exceptions

bucket_name = #バケット名を設定
print(f'Start create bucket {bucket_name}')

# リージョン情報の取得
session = boto3.session.Session()
resource = session.resource('s3')
current_region = session.region_name

# リソース API を使用
bucket = resource.Bucket(bucket_name)

try:
    bucket.create(
        CreateBucketConfiguration={
            'LocationConstraint': current_region
        }
    )

    waiter = resource.meta.client.get_waiter('bucket_exists')
    waiter.wait(Bucket=bucket_name)

    print('Bucket created.')

except botocore.exceptions.ClientError as e:
    print(e)
    print('Bucket creation failed.')
