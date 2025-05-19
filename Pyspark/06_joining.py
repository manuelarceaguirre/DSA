"""
1. transactions_df 
transactions
| Column          | Type    | Example Value         |
| --------------- | ------- | --------------------- |
| transaction_id | string  | "T001"                |
| customer_id    | string  | "C123"                |
| purchase_date  | string  | "2025-05-01 09:15:00" |
| item            | string  | "  Socks   "          |
| quantity        | integer | 2                     |
| price           | double  | 9.99                  |
| coupon_code    | string  | null / " SPRING2025"  |

2. customers_df (new), with the following columns:
customer_id	customer_name	loyalty_status
C1	Alice	Gold
C2	Bob	Silver
C3	Carol	Bronze

Perform a left join: Merge transactions_df (left) with customers_df (right) on customer_id.

The result DataFrame should include:

All columns from transactions_df

Columns customer_name and loyalty_status from customers_df

Display only those transactions that had a match in customers_df (i.e., inner join logic).
"""
from pyspark.sql import SparkSession
spark = SparkSession.builder.getOrCreate()

path = ""
transactions_df = spark.read.format("delta").load(path)
path2 = ""
customers_df = spark.read.format("delta").load(path2)
joined = transactions_df.join(customers_df,on = "customer_id", how = "inner")
result = joined.select(
    "transaction_id",
    "customer_id",
    "total_amount",
    "purchase_date_ts",
    "customer_name",
    "loyalty_status"
)
