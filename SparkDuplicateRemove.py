import findspark
findspark.init()

from pyspark.sql import SparkSession
spark = SparkSession.builder.master("local").appName("test").getOrCreate()
sc=spark.sparkContext

df = spark.read.csv("C:/Hadoop/SPARK/SPARK-PRACTICE/DuplicateRecords.csv", header=True, inferSchema=True)
df.printSchema()