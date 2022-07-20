import findspark
findspark.init()

from pyspark.sql import SparkSession
spark = SparkSession.builder.master("local").appName("test").getOrCreate()
sc=spark.sparkContext


data1 = (("Bob", "IT", 4500), \
("Maria", "IT", 4600), \
("James", "IT", 3850), \
("Maria", "HR", 4500), \
("James", "IT", 4500), \
("Sam", "HR", 3300), \
("Jen", "HR", 3900), \
("Jeff", "Marketing", 4500), \
("Anand", "Marketing", 2000),\
("Shaid", "IT", 3850) \
)
col=["Name", "MBA_STREAM","Marks"]
df=spark.createDataFrame(data1,col)
df.withColumn("marks", col("Marks").cast("integer"))
#df.show()
df.createOrReplaceTempView("students")
sqlDF = spark.sql("select * from students")
sqlDF.printSchema()

#findDF = sqlDF.select("Name", sqlDF['MARKS'].cast('Integer'))
#findDF.printSchema()
#findDF.show()


sc.stop()