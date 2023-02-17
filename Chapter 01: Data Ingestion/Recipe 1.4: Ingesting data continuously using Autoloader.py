# Databricks notebook source
df = (
 spark.readStream
 	  .format("cloudFiles")
      .option("cloudFiles.format","csv")
      .option("cloudFiles.schemaLocation", "/mnt/00-mchan-demo/databricks-cookbook/ch01_r04_schema/")
	  .option("header", "true")
   	  .option("inferSchema", "true")
	  .load("/mnt/00-mchan-demo/databricks-cookbook/ch01_r04/") 
      .writeStream
      .format("delta")
      .option("checkpointLocation", "/mnt/00-mchan-demo/databricks-cookbook/ch01_r04_checkpoint/")
      .trigger(availableNow = True)
      .outputMode("append")
      .toTable("t1_bronze_pos_sales")
)
