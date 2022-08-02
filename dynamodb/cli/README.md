## CLI サンプル

### 基本操作

```
# テーブルの一覧取得
aws dynamodb list-tables 

# テーブル作成
aws dynamodb create-table --table-name Notes --attribute-definitions="[{\"AttributeName\": \"UserId\", \"AttributeType\": \"S\"}, {\"AttributeName\": \"NoteId\", \"AttributeType\": \"N\"}]" --key-schema="[{\"AttributeName\": \"UserId\", \"KeyType\": \"HASH\"}, {\"AttributeName\": \"NoteId\", \"KeyType\": \"RANGE\"}]" --billing-mode="PAY_PER_REQUEST"

aws dynamodb wait table-exists --table-name Notes

aws dynamodb list-tables
```

### 項目の操作
```
# 項目の作成
aws dynamodb put-item --table-name Notes --item "{\"UserId\":{\"S\":\"StudentA\"},\"NoteId\":{\"N\":\"11\"},\"Note\":{\"S\":\"HelloWorld\"}}"

# 項目の削除
aws dynamodb delete-item --table-name Notes --key="{\"UserId\": {\"S\":\"StudentA\"}, \"NoteId\":{\"N\":\"11\"}}"
```

### DynamoDB Local
（事前に Docker Desktop 等をインストールし、コンテナ実行環境を準備しておく）
```
# 起動
docker run --name dynamodb -d -p 8000:8000 amazon/dynamodb-local   -jar DynamoDBLocal.jar -sharedDb

# アクセス（--endpoint-url を指定する以外は通常の DynamoDB と同様に操作可能）
aws dynamodb list-tables --endpoint-url http://localhost:8000

# 停止
docker stop dynamodb 

# 再起動
docker start dynamodb

# 削除
docker rm dynamodb

```

### NoSQL Workbench
以下からサイトからダウンロードリンクへアクセス可能
[NoSQL Workbench のダウンロード](https://docs.aws.amazon.com/ja_jp/amazondynamodb/latest/developerguide/workbench.settingup.html)