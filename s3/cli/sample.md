## CLI サンプル

### プロファイル作成

```
aws configure --profile プロファイル名
```

### プロファイルの変更
```
set AWS_PROFILE='プロファイル名'
#または
aws コマンド --profile プロファイル名
```

### 高レベル API
```
aws s3 ls # バケットの一覧取得
aws s3 mb  s3://バケット名 --region リージョン名 # バケットの作成
aws s3 sync s3://バケット名 ソースディレクトリ # バケットをローカルに同期 
aws s3 sync ソースディレクトリ s3://バケット名 # ローカルをバケットに同期
```

### 低レベル API
```
aws s3api バケット名 --query "Buckets[].Name" # バケットの一覧を取得
aws s3api get-bucket-location --bucket バケット名 # バケットのリージョンを取得
```

### プレフィックス
```
aws s3api list-objects --bucket notes-bucket --query Contents[].Key
# aws s3 ls s3://notes-bucket --recursive と同等

aws s3api list-objects --bucket notes-bucket --prefix Dev/  --query Contents[].Key
# aws s3 ls s3://notes-bucket/Dev/ --recursive と同等

aws s3api list-objects --bucket notes-bucket --prefix Dev/awsservice/ --delimiter "/"  --query "[Contents[].Key, CommonPrefixes[].Prefix]"
# aws s3 ls s3://notes-bucket/Dev/awsservice/ と同等
```

# バケット削除
```
aws s3 rb s3://バケット名
```
