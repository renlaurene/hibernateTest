#!/usr/bin/python

# Import modules for CGI handling 
import cgi, cgitb 
import pymysql

# Create instance of FieldStorage 
form = cgi.FieldStorage() 

# Get data from fields
song = form.getvalue('song')
cc_number = form.getvalue('cc_number')

print "Content-type:text/html\r\n\r\n"
print "<html>"
print "<head>"
print "<title>Hello - Second CGI Program</title>"
print "</head>"
print "<body>"
print "Successful"
print "</body>"
print "</html>"

#########################################
# Enter data to the table USER
#######################################
# Open database connection
db = pymysql.connect("localhost","root","yourpassword","which database" )

# Prepare a cursor object using cursor() method
cursor = db.cursor()

# Prepare SQL query to INSERT a record into the database.
sql = """INSERT INTO TRANSACTION(SONG,CC_NUMBER)
   VALUES ('""" + song +"""', '""" +  cc_number + """')"""
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Commit your changes in the database
   db.commit()
except:
   # Rollback in case there is any error
   db.rollback()

# disconnect from server
db.close()