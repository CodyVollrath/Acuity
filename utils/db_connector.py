import mysql.connector
class DbConnector:
    def __init__(self, host, user, password, schema):
        self.db = mysql.connector.connect(host=host,
                                     user=user,
                                     password=password)
        # db = mysql.connector.connect(host="wos-production3.cc5m4dlh7oxc.us-east-1.rds.amazonaws.com",
        #                                         user="WOSADMIN", password="HorseBarnes1!")
        self.cursor = self.db.cursor()
        self.cursor.execute(f'use {schema}')