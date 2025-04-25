import pandas as pd
import mysql.connector

#load data from csv file
df = pd.read_csv('data/AWCustomers.csv')

try:
#database connection 
    conn = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "yash",
        database = "insightsmith"
    )

    if conn.is_connected():
        print("connected to mysql database  successfully")
    
except mysql.connector.Error as e:
    print("error in connecting to mysql database",e)