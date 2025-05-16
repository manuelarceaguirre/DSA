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

Data Cleansing:
Trim whitespace from item and coupon_code columns.
Replace any null values in coupon_code with the string "NO_COUPON".
Remove duplicate rows (consider all columns for duplicates).
Data Enrichment:
Create a new column total_amount as quantity * price.
Create a new column purchase_date_ts as a proper timestamp type, converted from the string purchase_date.
"""


from pyspark.sql import SparkSession
spark = SparkSession.builder.getOrCreate()
from pyspark.sql import functions as F, timestamp

path = ""
transactions_df = spark.read.format("delta").load(path)
transactions_df = transactions_df.withColumn("item", F.trim(F.col("item")))
transactions_df = transactions_df.withColumn("coupon_code", F.trim(F.col("coupon_code")))
transactions_df = transactions_df.fillna({"coupon_code":"NO_COUPON"})
transactions_df = transactions_df.dropDuplicates()
transactions_df = transactions_df.withColumn(
        "total_amount",
        F.col("quantity") * F.col("price")
        )

transactions_df = transactions_df.withColumn(
        "purchase_date_ts",
        F.totimestamp(F.col("purchase_date"))
        )
