import os
from dotenv import load_dotenv
from src.spotify_etl import SpotifyETL

def load_environment() -> None:
    if os.path.exists("config/config.env"):
        load_dotenv(dotenv_path="config/config.env")
    else:
        raise FileNotFoundError("\"config/config.env\" not found")
    

def main() -> None:
    spotify_etl = SpotifyETL()
    spotify_etl.etl()

if __name__ == "__main__":
    load_environment()
    main()