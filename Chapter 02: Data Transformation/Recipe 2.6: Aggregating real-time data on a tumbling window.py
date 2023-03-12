# Databricks notebook source
# sample record: {"temp_recorded_time":"2023-01-01 01:10:00", "cooler_id": 102, "temp_celsius": 9.0}
from pyspark.sql.functions import *
from pyspark.sql.types import *

# group by operation on cooler_id
windowedAvgTempDF = (
    df.groupBy(window("temp_recorded_time", "5 minute") )
    .agg(round(avg("temp_celsius"), 2).alias("avg_temperature"))
)

# COMMAND ----------

display(windowedAvgTempDF)

# COMMAND ----------


