import os
from typing import final
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
from spotipy import util

from src.api_manager import APIManager
from src.database_manager import DatabaseManager
from src.util import HISTORY_TABLE_QUERY, get_date
from src.mail_manager import MailManager


class SpotifyETL():
    def __init__(self):
        self.api_manager = APIManager()
        self.db_manager = DatabaseManager()
        self.mail_manager = MailManager()

    def __del__(self):
        os.remove(self.fig)


    def daily_etl(self):
        
        # Get data from spotify api
        df = self.api_manager.get_recently_played_df()

        # DB
        self.db_manager.create_table(HISTORY_TABLE_QUERY)

        # Load df to db
        self.db_manager.df_to_sqlite(df=df, table_name='spotify_listen_history')


    def weekly_etl(self):
        # df = self.db_manager.read_table(table_name='listen_history_table')
        # Read weekly table
        df = self.__get_most_listened_song()

        # Create pie chart
        pie_chart = self.__pie_plot(df) 
        self.fig = 'weekly-pie.png'
        pie_chart.savefig(self.fig)

        #Send email
        subject = 'Last week spotify history!'
        receiver_mail = 'mertse7en7@gmail.com'
        image_path = self.fig
        self.mail_manager.send_mail(subject=subject, receiver=receiver_mail, img_path=image_path, html='template')


    def __get_most_listened_song(self):
        query = """
                SELECT song_name, artist_name, count(song_name) as count_song
                FROM spotify_listen_history 
                WHERE date BETWEEN '{}' AND '{}' 
                GROUP BY song_name 
                ORDER BY count(song_name) DESC
                """.format(get_date(days=7), get_date(days=0)) # Get data between last week and today
        
        df = self.db_manager.execute_query(query)

        return df.head(5)


    def __pie_plot(self, df):
        total_sum = sum(df["count_song"].tolist())
        count_percentile = [(i/total_sum)* 100 for i in df["count_song"].tolist()]
        labels =  df[["artist_name","song_name"]].agg(' - '.join, axis=1).tolist()
        explode = [0.1, 0, 0, 0, 0]

        plt.pie(count_percentile, labels = labels, explode = explode, shadow = True)

        return plt