# Databricks notebook source
# MAGIC %sql
# MAGIC CREATE OR REPLACE TABLE customer_orders AS SELECT
# MAGIC '{
# MAGIC    "items":{
# MAGIC       "fruits": [
# MAGIC         {"weight": 3,"type": "mango"},
# MAGIC         {"weight": 4,"type": "banana"}
# MAGIC       ],
# MAGIC       "books":[
# MAGIC         {
# MAGIC           "author": "John Smith",
# MAGIC           "title": "Fundamentals of Data",
# MAGIC           "category": "reference",
# MAGIC           "price": 7.95
# MAGIC         },
# MAGIC         {
# MAGIC           "author": "Mary Thomas",
# MAGIC           "title": "Data Fantasy",
# MAGIC           "category": "fiction",
# MAGIC           "price":9.99
# MAGIC         },
# MAGIC         {
# MAGIC           "author": "Rony Richmond",
# MAGIC           "title": "My Life in Data",
# MAGIC           "category": "biography",
# MAGIC           "price": 24.99
# MAGIC         }
# MAGIC       ],
# MAGIC       "toy_car":{
# MAGIC         "brand": "super wheels",
# MAGIC         "price": 9.99,
# MAGIC         "color": "red"
# MAGIC       }
# MAGIC     },
# MAGIC     "customer_name":"bob jones",
# MAGIC     "order_id":"12345"
# MAGIC  }' AS raw_data

# COMMAND ----------

# MAGIC %sql
# MAGIC -- Extract a top-level column to determine who placed the order -- 
# MAGIC SELECT 
# MAGIC   raw_data:customer_name, 
# MAGIC   raw_data:order_id,
# MAGIC   raw_data:items
# MAGIC FROM customer_orders

# COMMAND ----------

# MAGIC %sql
# MAGIC -- Extract nested fields through dot notation -- 
# MAGIC SELECT 
# MAGIC   raw_data:items.toy_car["brand"],
# MAGIC   raw_data:items.toy_car["price"],
# MAGIC   raw_data:items.toy_car["color"]
# MAGIC FROM customer_orders

# COMMAND ----------

# MAGIC %sql
# MAGIC -- Extract values from arrays through 0-based indexing 
# MAGIC SELECT 
# MAGIC   raw_data:items.books[*].author AS author,
# MAGIC   raw_data:items.books[*].title AS title,
# MAGIC   raw_data:items.books[*].category AS category,
# MAGIC   raw_data:items.books[*].price AS price
# MAGIC FROM customer_orders
