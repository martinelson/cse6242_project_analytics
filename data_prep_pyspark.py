from pyspark.context import SparkContext
from pyspark.sql.functions import col
from pyspark.sql import *
from pyspark.sql.functions import hour, when, col, date_format, to_timestamp
from pyspark.sql.functions import from_unixtime, unix_timestamp, col
from pyspark.sql.functions import *
from awsglue.dynamicframe import DynamicFrame
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.transforms import *
from pyspark.sql.functions import month, year,dayofmonth

def load_data():
    # Loads the data from S3 bucket and returns dataframe
    
    input_bucket = "s3://chicago-trip-data"
    trip_path = '/m6dm-c72p_*.csv'
    trips = spark.read.csv(input_bucket + trip_path, header=True, inferSchema=True)

    
    return trips



sc = SparkContext()
print("Starting load")
glueContext = GlueContext(sc)
spark = glueContext.spark_session
trips = load_data()

#replace column names space with "underscore"

replacements = {c:c.replace(' ','_') for c in trips.columns if ' ' in c}
trips=trips.select([col(c).alias(replacements.get(c, c)) for c in trips.columns])

#filter out records with NULL or 0 values for required columns

trips=trips.filter("Pickup_Community_Area is not NULL and Dropoff_Community_Area is not NULL and Trip_Total is not NULL and Trip_Total != 0 and Trip_Seconds is not NULL and Trip_Seconds != 0 and Fare > 0")

#add calculated attributes

trips = trips.withColumn('Trip_End_Timestamp',to_timestamp(col('Trip_End_Timestamp'),'MM/dd/yyyy hh:mm:ss aa'))
trips = trips.withColumn('Trip_Start_Timestamp',to_timestamp(col('Trip_Start_Timestamp'),'MM/dd/yyyy hh:mm:ss aa'))
trips = trips.withColumn("week_day", date_format(col("Trip_Start_Timestamp"), "EEEE")) #update this
trips = trips.withColumn('month',month("Trip_Start_Timestamp"))
trips = trips.withColumn('year',year("Trip_Start_Timestamp"))
trips = trips.withColumn('date',date_format(col("Trip_Start_Timestamp"),"MM/dd/yyyy"))
trips = trips.withColumn('week_year',date_format(col("Trip_Start_Timestamp"),"w"))  
trips = trips.withColumn('day_year',date_format(col("Trip_Start_Timestamp"),"D")) 
trips = trips.withColumn("hour", hour(col("Trip_Start_Timestamp")))  
trips = trips.withColumn("Trip_Seconds",col("Trip_Seconds").cast("decimal(38,0)"))
trips = trips.withColumn("Fare",col("Fare").cast('Float'))
trips = trips.withColumn("Tip",col("Tip").cast('Float'))
trips = trips.withColumn("total_revenue",col("Tip") + col("fare"))


#perform aggregates 

calc_trips=trips.groupBy('date','year','month','week_year','day_year','week_day','hour','Pickup_Community_Area').agg(sum("Trip_Miles"),sum("Trip_Seconds"),sum("Fare"),sum("Tip"),sum("total_revenue")
,sum("Additional_Charges"),sum("Trip_Total"),count("Fare"))


#rename columns

calc_trips=calc_trips.withColumnRenamed("Pickup_Community_Area", "pickup_community_area").withColumnRenamed("sum(Trip_Miles)","trip_miles_tot").withColumnRenamed("sum(Trip_Seconds)","trip_seconds_tot").withColumnRenamed("sum(Fare)","fare_tot").withColumnRenamed("sum(Tip)","tip_tot").withColumnRenamed("sum(total_revenue)","total_revenue").withColumnRenamed("sum(Additional_Charges)","additional_tot").withColumnRenamed("sum(Trip_Total)","trip_total_tot").withColumnRenamed("count(Fare)","count")


#select only needed columns
calc_trips=calc_trips.select("date","year","month","week_year","day_year","week_day","hour","pickup_community_area","count","trip_seconds_tot","trip_miles_tot","fare_tot","tip_tot","additional_tot","trip_total_tot","total_revenue")

#calculate counts
counts=calc_trips.count()
print("counts final",str(counts))

#save the results to s3 file
calc_trips.repartition(1).write.save("s3://chicago-trip-data/output_agg_results.csv", format='csv', header=True)
