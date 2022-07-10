import boto3
import botocore.exceptions

bucket_name = #バケット名を設定
key='notes.csv'

# クライアント API を使用
client = boto3.client('s3')
r = client.select_object_content(
    Bucket=bucket_name,
    Key=key,
    ExpressionType='SQL',
    Expression='select * from s3object s where s."UserId" = \'testuser\'',
    InputSerialization={'CSV': {"FileHeaderInfo" : "Use"}},
    OutputSerialization={'CSV': {}}
)

for event in r['Payload']:
    # print(event)
    if 'Records' in event:
        records = event['Records']['Payload'].decode('utf-8')
        print(records)
    elif 'Stats' in event:
        statsDetails = event['Stats']['Details']
        print(statsDetails)