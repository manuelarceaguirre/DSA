from pyspark.sql import SparkSession
spark = SparkSession.builder.getOrCreate()

from pyspark.sql.functions import sum
from pyspark.sql.functions import col
path = "/source/source/orders_daily"
df = spark.read.format("delta").load(path)

df.printSchema()
df.show(5)

# filtering
df_filtered = df.filter(df["status"] == "COMPLETE")
# aggregating
df_agg = df_filtered.groupBy("region").agg(sum("sales").alias("total_sales"))

# check row count
if df_agg.count() < 100:
    raise Exception ("Too few rows")

# check if there are null values in the sales column 
if df_filtered.filter(col("sales").isNull()).count() > 0:
    raise Exception("Null detected in sales column")

df_agg.write.format("delta").mode("overwrite").save(path)

