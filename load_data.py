import pandas as pd
import mysql.connector

#load data from csv file
df = pd.read.csv('data\AWCustomers.csv')

#database connection 
conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "1234",
    database = "insightsmith"
)