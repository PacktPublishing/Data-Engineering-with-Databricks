# Databricks notebook source
# MAGIC %sql
# MAGIC CREATE OR REPLACE TABLE dim_employees_scdtype3 (
# MAGIC   employee_id INT,
# MAGIC   employee_name VARCHAR(100),
# MAGIC   job_title VARCHAR(100),
# MAGIC   previous_job_title VARCHAR(100),
# MAGIC   payband VARCHAR(100),
# MAGIC   previous_payband VARCHAR (100)
# MAGIC );
# MAGIC 
# MAGIC INSERT INTO dim_employees_scdtype3 (employee_id, employee_name, job_title, previous_job_title, payband, previous_payband)
# MAGIC VALUES (1, "John Smith", "Data Analyst", NULL,"L5",NULL),
# MAGIC        (2, "Stu Jones", "VP of Analytics", NULL,"L7",NULL),
# MAGIC        (3, "Bob Belson", "Business Analyst", NULL,"L5",NULL),
# MAGIC        (4, "Maddy Moore", "Data Engineer", NULL,"L6", NULL),
# MAGIC        (5, "Chris Coxwell", "IT Director", NULL,"L5", NULL);

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * 
# MAGIC FROM dim_employees_scdtype3;

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
# MAGIC MERGE INTO dim_employees_scdtype3 t1
# MAGIC USING employee_updates t2 
# MAGIC ON t1.employee_id = t2.employee_id
# MAGIC WHEN MATCHED THEN UPDATE SET t1.previous_job_title = t1.job_title,
# MAGIC                              t1.previous_payband = t1.payband,
# MAGIC                              t1.job_title = t2.job_title,
# MAGIC                              t1.payband = t2.payband
# MAGIC WHEN NOT MATCHED THEN INSERT (
# MAGIC                               employee_id,
# MAGIC                               employee_name,
# MAGIC                               job_title,
# MAGIC                               previous_job_title,
# MAGIC                               payband,
# MAGIC                               previous_payband)
# MAGIC                       VALUES (
# MAGIC                               t2.employee_id,
# MAGIC                               t2.employee_name,
# MAGIC                               t2.job_title,
# MAGIC                               NULL,
# MAGIC                               t2.payband,
# MAGIC                               NULL);

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * 
# MAGIC FROM dim_employees_scdtype3
# MAGIC ORDER BY employee_id;

# COMMAND ----------


