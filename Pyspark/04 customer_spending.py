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

Filter the DataFrame to include only transactions where total_amount is greater than or equal to 20.
Group the filtered data by customer_id and calculate:
The total number of transactions per customer (call the column num_transactions)
The total spend per customer (sum of total_amount)
The most recent purchase (max of purchase_date_ts)
Requirements:
Use PySpark DataFrame API (not Spark SQL).
"""
from pyspark.sql import SparkSession
spark = SparkSession.builder.getOrCreate()
from pyspark.sql import functions as F 

path = ""
transactions_df = spark.read.format("delta").load(path)
transactions_filtered = transactions_df.filter(F.col("total_amount") >= 20)

transactions_agg = transactions_filtered.groupBy("customer_id").agg(
        F.count("transaction_id").alias("total_transaction"),
        F.sum("total_amount").alias("total_spend"),
        F.max("purchase_date_ts").alias("most_recent")
)
