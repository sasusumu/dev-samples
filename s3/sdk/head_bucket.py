import boto3
import botocore.exceptions


bucket_name = #バケット名を設定
print(f'Check bucket {bucket_name}')

## インスタンスプロファイルを使用して認証情報を取得
session = boto3.session.Session()
resource = session.resource('s3')
current_region = session.region_name

## head_bucket はクライアント API として提供されている
client = boto3.client('s3')

## head_bucket を実行。バケットが存在すれば正常に処理が終了、存在しなかった場合 例外が発生する
try:
    client.head_bucket(
        Bucket=bucket_name
    )
    print('This bucket has already been created')
except botocore.exceptions.ClientError as e:
	error_code = int(e.response['Error']['Code'])
	if error_code == 404:
		## 404 エラーコードを受信した場合、その名前のバケットは
		## AWS には存在しない
		print('Existing Bucket Not Found, please proceed')
	if error_code == 403:
	# 	## 403 エラーコードを受信した場合、その名前のバケットは 
	# 	## 別の AWS アカウントに存在する
	    print('This bucket has already owned by another AWS Account')
