# Databricks notebook source
# MAGIC %sql
# MAGIC CREATE OR REPLACE TABLE dim_employees_scdtype1 (
# MAGIC   employee_id INT,
# MAGIC   employee_name VARCHAR(100),
# MAGIC   job_title VARCHAR(100),
# MAGIC   payband VARCHAR(100)
# MAGIC );
# MAGIC 
# MAGIC INSERT INTO dim_employees_scdtype1 (employee_id, employee_name, job_title, payband)
# MAGIC VALUES (1, "John Smith", "Data Analyst", "L5"),
# MAGIC        (2, "Stu Jones", "VP of Analytics", "L7"),
# MAGIC        (3, "Bob Belson", "Business Analyst", "L5"),
# MAGIC        (4, "Maddy Moore", "Data Engineer", "L6"),
# MAGIC        (5, "Chris Coxwell", "IT Director", "L5");

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT *
# MAGIC FROM dim_employees_scdtype1;

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
# MAGIC MERGE INTO dim_employees_scdtype1 t1 
# MAGIC USING employee_updates t2 
# MAGIC ON t1.employee_id = t2.employee_id
# MAGIC WHEN MATCHED THEN UPDATE SET * 
# MAGIC WHEN NOT MATCHED THEN INSERT * 

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * 
# MAGIC FROM dim_employees_scdtype1
# MAGIC ORDER BY employee_id;
