import datetime
import os, sys
import pandas as pd
import sqlite3
import logging


logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(name)s - %(funcName)s - %(message)s")



class DatabaseManager:
    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)

        # Configure gcp
        from sqlalchemy import create_engine
        self.conn = sqlite3.connect("spotify.db")
        self.cursor = self.conn.cursor() 



    def create_table(self, query):
        self.cursor.execute(query)
        self.logger.info("Table has been successfuly created !")


    def df_to_sqlite(self, df, table_name):
        df.to_sql(table_name, self.conn, if_exists='append', index=False)
        self.conn.commit()
        self.logger.info("Inserted !")


    def read_table(self, table_name):
        query = "SELECT * FROM {}".format(table_name)
        df = pd.read_sql(query, self.conn)
        return df


    def execute_query(self, query):
        df = pd.read_sql(query, self.conn)
        return df