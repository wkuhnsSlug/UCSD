

import pyspark
from pyspark.context import SparkContext
from pyspark.sql.context import SQLContext
from pyspark.sql.session import SparkSession
from urllib.request import urlretrieve

import findspark
findspark.init("C:\\Users\\Will\\PycharmProjects\\pandaPractice\\venv\\Lib\\site-packages\\pyspark")

sc = pyspark.SparkContext("community.cloud.databricks.com:443", "SQL stuff")
sqlContext = SQLContext(sc)
spark = SparkSession(sc)

def run_sql(statement):
    try:
        result = sqlContext.sql(statement)
    except Exception as e:
        print(e.desc, '\n', e.stackTrace)
        return
    return result

run_sql('drop database if exists country_club cascade')
run_sql('create database country_club')
dbs = run_sql('show databases')
dbs.toPandas()



# File location and type
file_location_bookings = "./Bookings.csv"
file_location_facilities = "./Facilities.csv"
file_location_members = "./Members.csv"

file_type = "csv"

# CSV options
infer_schema = "true"
first_row_is_header = "true"
delimiter = ","

# The applied options are for CSV files. For other file types, these will be ignored.
bookings_df = (spark.read.format(file_type)
                    .option("inferSchema", infer_schema)
                    .option("header", first_row_is_header)
                    .option("sep", delimiter)
                    .load(file_location_bookings))

facilities_df = (spark.read.format(file_type)
                      .option("inferSchema", infer_schema)
                      .option("header", first_row_is_header)
                      .option("sep", delimiter)
                      .load(file_location_facilities))

members_df = (spark.read.format(file_type)
                      .option("inferSchema", infer_schema)
                      .option("header", first_row_is_header)
                      .option("sep", delimiter)
                      .load(file_location_members))

print('Bookings Schema')
bookings_df.printSchema()
print('Facilities Schema')
facilities_df.printSchema()
print('Members Schema')
members_df.printSchema()



permanent_table_name_bookings = "country_club.Bookings"
bookings_df.write.format("parquet").saveAsTable(permanent_table_name_bookings)

permanent_table_name_facilities = "country_club.Facilities"
facilities_df.write.format("parquet").saveAsTable(permanent_table_name_facilities)

permanent_table_name_members = "country_club.Members"
members_df.write.format("parquet").saveAsTable(permanent_table_name_members)

run_sql('use country_club')
run_sql('REFRESH table bookings')
run_sql('REFRESH table facilities')
run_sql('REFRESH table members')
tbls = run_sql('show tables')
tbls.toPandas()



result = run_sql('''
                    SELECT * 
                    FROM bookings 
                    LIMIT 3
                 ''')
result.toPandas()

result = run_sql('''
                    SELECT name
                    FROM facilities
                        WHERE facilities.membercost = 0

                 ''')
result.toPandas()

result = run_sql('''
                    SELECT COUNT(name)
                    FROM facilities
                        WHERE membercost = 0

                 ''')
result.toPandas()

result = run_sql('''
                    SELECT facid, name, membercost, monthlymaintenance
                    FROM facilities
                        WHERE membercost > 0
                        AND (membercost / monthlymaintenance) < 0.2

                ''')
result.toPandas()

result = run_sql('''
                    SELECT *
                    FROM facilities
                        WHERE facid IN (1, 5)
                ''')
result.toPandas()

result = run_sql('''
                    SELECT name, monthlymaintenance,
                        CASE WHEN monthlymaintenance > 100 THEN 'expensive'
                        ELSE 'cheap' END
                        AS relative_cost
                    FROM facilities
                 ''')
result.toPandas()

result = run_sql('''
                    SELECT firstname, surname
                    FROM members
                        WHERE joindate = (SELECT MAX(joindate) FROM members)
                 ''')
result.toPandas()

result = run_sql('''
                    SELECT DISTINCT CONCAT(surname, ', ', firstname) AS member, name AS facility
                    FROM members AS m
                        INNER JOIN bookings AS b
                            ON m.memid = b.memid
                            AND m.memid != '0'
                        INNER JOIN facilities AS f
                            ON f.facid = b.facid
                            WHERE b.facid IN (0, 1)
                            ORDER BY member ASC
                 ''')
result.toPandas()


result = run_sql('''
                    SELECT CONCAT(surname, ', ', firstname) AS member, name AS facility,
                        CASE WHEN b.memid == 0 THEN (b.slots * f.guestcost)
                        ELSE (b.slots * f.membercost) END
                        AS cost
                    FROM members AS m
                        INNER JOIN bookings AS b
                            ON m.memid = b.memid
                        INNER JOIN facilities AS f
                            ON f.facid = b.facid
                            WHERE Date(b.starttime) = '2012-09-14'
                            AND
                              (
                                CASE WHEN b.memid == 0 THEN (b.slots * f.guestcost)
                                ELSE (b.slots * f.membercost) END
                              ) > 30
                            ORDER BY cost DESC
                 ''')
result.toPandas()

result = run_sql('''SELECT member, facility, cost FROM
                        (
                            SELECT CONCAT(surname, ', ', firstname) AS member, name AS facility,
                                CASE WHEN b.memid == 0 THEN (b.slots * f.guestcost)
                                ELSE (b.slots * f.membercost) END
                                AS cost FROM members AS M
                                INNER JOIN bookings AS b
                                    ON m.memid = b.memid
                                INNER JOIN facilities AS f
                                    ON f.facid = b.facid
                                    WHERE Date(b.starttime) = '2012-09-14'
                        )
                        AS tmp
                            WHERE cost > 30
                            ORDER BY cost DESC
                 ''')
result.toPandas()

result = run_sql('''SELECT facility, SUM(cost) AS revenue FROM
                        (
                            SELECT name AS facility,
                                CASE WHEN b.memid == 0 THEN (b.slots * f.guestcost)
                                ELSE (b.slots * f.membercost) END
                                AS cost FROM members AS M
                                INNER JOIN bookings AS b
                                    ON m.memid = b.memid
                                INNER JOIN facilities AS f
                                    ON f.facid = b.facid
                        )
                        AS tmp
                        GROUP BY facility
                            HAVING revenue < 1000
                        ORDER BY revenue DESC
                 ''')
result.toPandas()