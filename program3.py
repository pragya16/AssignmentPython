# Question 3:Write a python standalone program a. insert some values [eg. employee details]in db tab b. fetch the same data and print it on standard output.c. update specific employee info.d. delete specific employee and all the info.

import sqlite3

conn = sqlite3.connect('emp3.db')
print "Opened database successfully";
# prepare a cursor object using cursor() method
cursor = conn.cursor()

# Create table as per requirement
sql = """CREATE TABLE EMPLOYEE4 (
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20),
         AGE INT,  
         SEX CHAR(1),
         INCOME FLOAT )"""

cursor.execute(sql)
print "table create successfully"

# insert value in table
cursor.execute ("INSERT INTO EMPLOYEE4 (FIRST_NAME, LAST_NAME, AGE, SEX ,INCOME) 
      VALUES ('pragya', 'Gupta', 24, 'female', 20000.00 ");
print "Records insertsuccessfully"

#display data
cursor.execute ("SELECT FIRST_NAME, LAST_NAME, AGE, SEX ,INCOME from EMPLOYEE4 ")
for row in cursor:
   print "FIRST_NAME = ", row[0]
   print "LAST_NAME = ", row[1]
   print "AGE = ", row[2]
   print "SEX = ", row[3]
   print "INCOME= ", row[4],"\n"
conn.commit()
print "Operation done successfully"

#update
cursor.execute("UPDATE EMPLOYEE4 set INCOME=25000 where FIRST_NAME='pragya'")
conn.commit()
print "Records update successfully";

# delete
cursor.execute("DELETE from EMPLOYEE4 where LAST_NAME = 'Gupta'")
conn.commit()

print "Records distroy successfully";
conn.close()
