[Python 実践データ分析100本ノック](https://www.shuwasystem.co.jp/support/7980html/7566.html)

```PowerShell
ni .gitignore -ItemType File
```

## Gitリポジトリとして初期化
```
git init
```

## ファイルを追跡対象に追加
```
git add .
```

## データの結合

### 縦方向に結合（ユニオン）

同じ列構成のデータを上下に連結します。

```python
result = pd.concat(
    [transaction_1, transaction_2],
    ignore_index=True
)
```

### 横方向に結合（ジョイン）

共通のキーを使って、別のデータが持つ列を結合します。

```python
result = pd.merge(
    transaction,
    customer_master,
    on="customer_id",
    how="left"
)
```

- `pd.concat()`：複数のデータを並べて連結する
- `pd.merge()`：共通キーを基準に結合する
- `ignore_index=True`：結合後の行番号を振り直す
- `how="left"`：左側のデータを基準に結合する
