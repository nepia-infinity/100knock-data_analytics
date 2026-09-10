import pandas as pd
from datetime import datetime
from zoneinfo import ZoneInfo

# 売上データの読み込み
transaction_1 = pd.read_csv("100knock-data_analytics/1章/transaction_1.csv")
transaction_2 = pd.read_csv("100knock-data_analytics/1章/transaction_2.csv")
print(f'transaction_1: {len(transaction_1)} 件')
print(f'transaction_2: {len(transaction_2)} 件')

# 売上明細データの結合
transaction_detail_1 = pd.read_csv("100knock-data_analytics/1章/transaction_detail_1.csv")
transaction_detail_2 = pd.read_csv("100knock-data_analytics/1章/transaction_detail_2.csv")
print(f'transaction_detail_1: {len(transaction_detail_1)} 件')
print(f'transaction_detail_2: {len(transaction_detail_2)} 件')

# 縦方向の結合（例）月次のデータをまとめる場合などに使用する
transaction_merged = pd.concat([transaction_1, transaction_2], ignore_index=True)
print(f'transaction_merged: {len(transaction_merged)} 件')
# print(transaction_merged.head())

transaction_detail_merged = pd.concat([transaction_detail_1, transaction_detail_2], ignore_index=True)
print(f'transaction_detail_merged: {len(transaction_detail_merged)} 件')
# print(transaction_detail_merged.head())

joined_data = pd.merge(transaction_merged[['transaction_id','payment_date','customer_id']], transaction_detail_merged, on='transaction_id', how='left')
print(f'joined_data: {len(joined_data)} 件')
print(joined_data.head())

# 結合したデータをExcelに出力
timestamp = datetime.now(
    ZoneInfo("Asia/Tokyo")
).strftime("%Y%m%d_%H%M%S")

file_name = f"joined_data_{timestamp}.xlsx"
joined_data.to_excel(file_name, index=False)
