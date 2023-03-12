# Databricks notebook source
# MAGIC %sql
# MAGIC CREATE OR REPLACE TABLE dim_employees_scdtype2 (
# MAGIC   employee_id INT,
# MAGIC   employee_name VARCHAR(100),
# MAGIC   job_title VARCHAR(100),
# MAGIC   payband VARCHAR(100),
# MAGIC   start_date DATE,
# MAGIC   end_date DATE,
# MAGIC   status VARCHAR (10)
# MAGIC );
# MAGIC 
# MAGIC INSERT INTO dim_employees_scdtype2 (employee_id, employee_name, job_title, payband, start_date, end_date, status)
# MAGIC VALUES (1, "John Smith", "Data Analyst", "L5", "2023-01-01", NULL, "Current"),
# MAGIC        (2, "Stu Jones", "VP of Analytics", "L7", "2023-01-01",NULL, "Current"),
# MAGIC        (3, "Bob Belson", "Business Analyst", "L5", "2023-01-01",NULL, "Current"),
# MAGIC        (4, "Maddy Moore", "Data Engineer", "L6", "2023-01-01",NULL, "Current"),
# MAGIC        (5, "Chris Coxwell", "IT Director", "L5", "2023-01-01",NULL, "Current");

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * 
# MAGIC FROM dim_employees_scdtype2;

# COMMAND ----------

# MAGIC %sql
# MAGIC -- new snapshot ingested from the source HR database -- 
# MAGIC CREATE OR REPLACE TABLE employee_updates (
# MAGIC   employee_id INT,
# MAGIC   employee_name VARCHAR(100),
# MAGIC   job_title VARCHAR(100),
# MAGIC   payband VARCHAR(100)
# MAGIC );
# MAGIC 
# MAGIC INSERT INTO employee_updates (employee_id, employee_name, job_title, payband)
# MAGIC VALUES (1, "John Smith", "Senior Data Analyst", "L6"),
# MAGIC        (2, "Stu Jones", "CIO", "L8"),
# MAGIC        (6, "Mary Timms", "Data Governance Steward", "L5");
# MAGIC 
# MAGIC SELECT * 
# MAGIC FROM employee_updates;

# COMMAND ----------

# MAGIC %sql
# MAGIC MERGE INTO dim_employees_scdtype2 t1 
# MAGIC USING 
# MAGIC (
# MAGIC   SELECT t2.employee_id AS mergeKey,
# MAGIC          t2.employee_id,
# MAGIC          t2.employee_name, 
# MAGIC          t2.job_title, 
# MAGIC          t2.payband, 
# MAGIC          current_date() AS start_date, 
# MAGIC          "" AS end_date, 
# MAGIC          "Current" AS status
# MAGIC   FROM employee_updates t2 
# MAGIC   UNION ALL 
# MAGIC   SELECT NULL AS mergeKey,
# MAGIC          t2.employee_id,
# MAGIC          t2.employee_name, 
# MAGIC          t2.job_title, 
# MAGIC          t2.payband, 
# MAGIC          current_date() AS start_date, 
# MAGIC          "" AS end_date, 
# MAGIC          "Current" AS status
# MAGIC   FROM employee_updates t2
# MAGIC ) t3
# MAGIC ON t1.employee_id = t3.mergeKey 
# MAGIC AND t1.status = "Current"
# MAGIC WHEN MATCHED THEN UPDATE SET t1.status = "Expired", t1.end_date = t3.start_date
# MAGIC WHEN NOT MATCHED AND mergeKey IS NULL THEN INSERT * 

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * 
# MAGIC FROM dim_employees_scdtype2;
