"""
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
Rank their transactions by purchase_date_ts (most recent first).
Calculate a running total of total_amount across each customer’s purchases, ordered by purchase date (earliest to latest).
Produce a final DataFrame containing:
customer_id
transaction_id
purchase_date_ts
total_amount
transaction_rank (1 = most recent)
running_total_amount
"""
from pyspark.sql import SparkSession
spark = SparkSession.builder.getOrCreate()
from pyspark.sql import functions as F 
from pyspark.sql import Window
path = ""
transactions_df = spark.read.format("delta").load(path)
window_rank = Window.partitionBy("customer_id").orderBy("purchase_date_ts")

transactions_df = transactions_df.withColumn(
        "ranking",
        F.row_number().over(window_rank)
        )
window_amount = Window.partitionBy("customer_id").orderBy("purchase_date_ts").rowsBetween(Window.unboundedPreceding, Window.currentRow)

transactions_df = transactions_df.withColumn(
        "total_running",
        F.sum("total_amount").over(window_amount)
        )
transactions_df.select(
"customer_id",
"transaction_id",
"purchase_date_ts",
"total_amount",
"ranking",
"total_running"
        )
