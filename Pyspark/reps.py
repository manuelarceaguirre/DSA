
"""
/mnt/source/orders
Column	Type
order_id	string
customer_id	string
product	string
amount	float
status	string
order_date	date

/mnt/source/customers
Column	Type
customer_id	string
region	string
signup_date	date
"""

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, avg, year, date_format
spark = SparkSession.builder.getOrCreate()

orders_path = '/mnt/source/orders'
customers_path = '/mnt/source/customers'

df_orders = spark.read.format("delta").load(orders_path)
df_customers = spark.read.format("delta").load(customers_path)

filtered_orders = df_orders.filter(
        (col("status") == "COMPLETE") &
        (year(col("order_date")) == 2023)
)

orders_and_customers = filtered_orders.join(df_customers,on = "customer_id", how = "inner")
orders_and_customers = orders_and_customers.withColumn("order_month",date_format("order_month", "yyyy-MM"))

monthly_avg = orders_and_customers.groupBy("region","order_month").agg(avg("amount").alias("avg_order_amount"))
monthly_avg.write.format("delta").load("/mnt/target/avg_monthly_orders_by_region")

"""
Calculate Running Total of Orders by Customer
Dataset: /mnt/source/orders
Column	Type
order_id	string
customer_id	string
product	string
amount	float
status	string
order_date	date
"""

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, avg, year, date_format
spark = SparkSession.builder.getOrCreate()
path = "/mnt/source/orders"
df_orders = spark.read.format("delta").load()
filtered_orders = df_orders.filter(col("status") == "COMPLETE")
filtered_orders.groupBy(col("customer_id")).sort(col("order_date"))
if filtered_orders(col("amount") == None):
    raise Exception("value in amount is Null")
filtered_orders.withColumn("running_total").sum(col("amount"))
filtered_orders.select(col("customer_id") & col("order_id") & col("order_date") & col("amount") & col("running_total"))
filtered_orders.write.format("delta").load("/mnt/target/orders_running_total")

"""
/mnt/source/orders
Column	Type
order_id	string
customer_id	string
product	string
amount	float
status	string
order_date	date

/mnt/source/customers
Column	Type
customer_id	string
region	string
signup_date	date
"""

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, avg, year, date_format
from datetime import datetime, timedelta
path_orders = "/mnt/source/orders"
path_customers = "/mnt/source/customers"
path_output = "/mnt/target/top_product_by_region_recent"
df_orders = spark.read.format("delta").load(path_orders)
df_customers = spark.read.format("delta").load(path_customers)

# filter
df_orders_completed = df_orders.filter(
        col("status") == "COMPLETE",
        order_date = date_format.format("yyyy-MM")
)
# date filter
ninety_days_ago = (datetime.today() - timedelta(days=90)).strftime("%Y-%m-%d")
df_90 = df_orders_completed.filter(col("order_date") - today <= 90) 

# join 
joined = df_90.join(df_customers,on="customer_id")

top_selling_product = joined.agg(col("region")).sum(col("amount"))


top_selling_product.load.format("delta").load(path_output)















