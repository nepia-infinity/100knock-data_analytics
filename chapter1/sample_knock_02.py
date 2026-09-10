import pandas as pd
transaction_1 = pd.read_csv("100knock-data_analytics/1章/transaction_1.csv")
transaction_2 = pd.read_csv("100knock-data_analytics/1章/transaction_2.csv")
print(f'transaction_1: {len(transaction_1)} 件')
print(f'transaction_2: {len(transaction_2)} 件')

# 縦方向の結合
transaction_merged = pd.concat([transaction_1, transaction_2], ignore_index=True)
print(f'transaction_merged: {len(transaction_merged)} 件')