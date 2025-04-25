import pandas as pd
import mysql.connector

#load data from csv file
df = pd.read.csv('data\AWCustomers.csv')

try:
#database connection 
    conn = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "1234",
        database = "insightsmith"
    )

    if conn.is_connected():
        print("connected to mysql database  successfully")
    
except:
    print("error in connecting to mysql database")