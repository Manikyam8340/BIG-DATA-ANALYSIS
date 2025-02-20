from pyspark.sql import SparkSession
from pyspark.sql.functions import col, count, avg, desc

# Initialize Spark Session
spark = SparkSession.builder \
    .appName("Big Data Analysis") \
    .getOrCreate()

# Load Dataset 
data_path = "path/to/your/large_dataset.csv"
df = spark.read.csv(data_path, header=True, inferSchema=True)

# Display Schema
df.printSchema()

# Basic Statistics
total_rows = df.count()
print(f"Total Rows in Dataset: {total_rows}")

# Data Exploration - Top 5 most common categories 
categories_count = df.groupBy("category").agg(count("*").alias("count"))
categories_count_sorted = categories_count.orderBy(desc("count"))
categories_count_sorted.show(5)

# Compute Average Value of a Numeric Column 
average_price = df.select(avg(col("price")).alias("avg_price"))
average_price.show()

# Save Processed Data (Optional)
categories_count_sorted.write.csv("output/category_counts.csv", header=True)
# stop
spark.stop()