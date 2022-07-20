import findspark
findspark.init()

from pyspark import SparkContext, SparkConf, SQLContext

appName = "PySpark SQL Server Example - via JDBC"
master = "local"
conf = SparkConf() \
    .setAppName(appName) \
    .setMaster(master) \
    .set("spark.driver.extraClassPath","C:/bigdata/spark3/jars/mssql-jdbc-10.2.1.jre8.jar")
sc = SparkContext(conf=conf)
sqlContext = SQLContext(sc)
spark = sqlContext.sparkSession

database = "TestData"
table = "dbo.employees"
user = "root1"
password  = "root1"

jdbcDF = spark.read.format("jdbc") \
    .option("url", f"jdbc:sqlserver://localhost:1433;databaseName={database}") \
    .option("dbtable", "Employees") \
    .option("user", user) \
    .option("password", password) \
    .option("driver", "com.microsoft.sqlserver.jdbc.SQLServerDriver") \
    .load()

jdbcDF.show()