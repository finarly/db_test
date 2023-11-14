# Databricks notebook source
# MAGIC %md
# MAGIC # Notebook to help analyse the data

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC -- Which artists released the most songs each year?
# MAGIC SELECT
# MAGIC   artist_name,
# MAGIC   count(artist_name)
# MAGIC AS
# MAGIC   num_songs,
# MAGIC   year
# MAGIC FROM
# MAGIC   new_raw_song_data
# MAGIC WHERE
# MAGIC   year > 0
# MAGIC GROUP BY
# MAGIC   artist_name,
# MAGIC   year
# MAGIC ORDER BY
# MAGIC   num_songs DESC,
# MAGIC   year DESC

# COMMAND ----------

# MAGIC  %sql
# MAGIC  -- Find songs for your DJ list
# MAGIC  SELECT
# MAGIC    artist_name,
# MAGIC    title,
# MAGIC    tempo
# MAGIC  FROM
# MAGIC new_raw_song_data WHERE
# MAGIC    time_signature = 4
# MAGIC    AND
# MAGIC    tempo between 100 and 140;

# COMMAND ----------


