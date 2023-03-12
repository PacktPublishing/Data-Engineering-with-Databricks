# Databricks notebook source
# sample record: {"temp_recorded_time":"2023-01-01 01:10:00", "cooler_id": 102, "temp_celsius": 9.0}
from pyspark.sql.functions import *
from pyspark.sql.types import *

schema = StructType(
  [
    StructField("temp_recorded_time", TimestampType()),
    StructField("cooler_id", IntegerType()),
    StructField("temp_celsius", FloatType())    
  ]
)

# COMMAND ----------

# replace with your own cloud storage path 
s3FilePath = "/mnt/databricks-cookbook/ch02_r05/"

df = (
  spark.readStream
       .format("cloudFiles")
       .option("cloudFiles.format", "json")
       .schema(schema)
       .load(s3FilePath)
)

# COMMAND ----------

display(df)

# COMMAND ----------

# group by operation on cooler_id
avgTempDF = (
  df.groupBy("cooler_id")
    .agg(round(avg("temp_celsius"), 2).alias("avg_temperature"))
)

# COMMAND ----------

display(avgTempDF)
