"""
For reporting, we need a daily table of high-value orders (amount > 500) 
enriched with customer region. This will be part of an Airflow DAG 
and should overwrite the partition for the current day each time it runs.

/mnt/source/orders
Column	Type
order_id	string
customer_id	string
amount	float
order_date	date

/mnt/source/customers
Column	Type
customer_id	string
region	string
signup_date	date
"""

from pyspark.sql import SparkSession
spark = SparkSession.builder.getOrCreate()
from pyspark.sql.functions import col
from datetime import datetime
# paths 
orders_path = "/mnt/source/orders"
customers_path = "/mnt/source/customers"
output_path = "/mnt/target/high_value_orders_daily"

# load
orders_df = spark.read.format("delta").load(orders_path)
customers_df = spark.read.format("delta").load(customers_path)

# orders amount > 500
orders_df_filter_amount = orders_df.filter(col("amount") > 500)
# today's date
today_str = datetime.today().strftime("%Y-%m-%d")
orders_df_filter_amount_today = orders_df_filter_amount.filter(col("order_date") == today_str)
# join
orders_enriched = orders_df_filter_amount_today.join(customers_df, on = "customer_id")
orders_enriched.write.format("delta").mode("overwrite").partitionBy("order_date").save(output_path)
