import datetime

HISTORY_TABLE_QUERY = """
        CREATE TABLE IF NOT EXISTS spotify_listen_history(
            song_name TEXT,
            artist_name TEXT ,
            song_id INTEGER,
            song_popularity INTEGER,
            song_preview_url TEXT,
            song_spotify_url TEXT,
            album_name TEXT,
            album_id INTEGER,
            album_spotify_url TEXT,
            artist_id INTEGER,
            artist_spotify_url TEXT,
            date DATE);
        """

def get_date(days=1, direction='negative', date_format='%Y-%m-%d'):
        if direction == 'negative':
            today = datetime.datetime.today()
            from_day = (today - datetime.timedelta(days=days)).strftime(date_format)

            return today.strftime(date_format) if days==0 else from_day
        elif direction == 'positive' : # direction positive
            today = datetime.datetime.today()
            from_day = (today + datetime.timedelta(days=days)).strftime(date_format)

            return from_day


