"""
/mnt/source/orders
order_id, customer_id, product, amount, order_date
/mnt/source/customers
customer_id, region

Create a new pipeline to calculate the
average number of products per order for
each region and week over the last 6 months.
Use orders and customers tables.
Output should be stored to Delta table at /mnt/target/avg_items_per_order.
"""
from pyspark.sql import SparkSession
spark = SparkSession.builder.getOrCreate()
from datetime import datetime, timedelta
from pyspark.sql.functions import col, weekofyear, count, countDistinct
# load
output = "/mnt/target/avg_items_per_order"
orders_path = "/mnt/source/orders"
customers_path = "/mnt/source/customers"

orders_df = spark.read.format("delta").load(orders_path)
customers_df = spark.read.format("delta").load(customers_path)

# filter last 6 months
six_months_ago = (datetime.today() - timedelta(days = 180))
orders_filtered = orders_df.filter(col("order_date") > six_months_ago)

# new column week
orders_filtered = orders_filtered.withColumn("week", weekofyear(col("order_date")))

# join
customers_and_orders = orders_filtered.join(customers_df, on = "customer_id")

# agg
agg_customers_and_orders = customers_and_orders.groupBy("region", "week").agg(
        (count("amount") / countDistinct("order_id")).alias("avg_items_per_order")
        )
agg_customers_and_orders = agg_customers_and_orders.orderBy("region", "week")
